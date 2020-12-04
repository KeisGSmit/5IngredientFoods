# Importing the required frameworks
import os
import json
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# Intialising the app and getting environment variables
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')


mongo = PyMongo(app)


# register app route
@app.route("/register", methods=["GET", "POST"])
def register():
    # user submits form to register
    if request.method == "POST":
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
            )
        # if the user exists, return a flash message
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # create a dictionary with the input username and password 
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # insert the dictionary into the collection
        mongo.db.users.insert_one(register)

        # put the user into the current "session" - like a cookie
        session["user"] = request.form.get("username").lower()
        # flash a message to the user
        flash("Registration Successful")
        return redirect(url_for('home', username=session["user"]))

    return render_template("register.html")


# login app route
@app.route("/login", methods=["GET", "POST"])
def login():
    # user submits a username and password 
    if request.method == "POST":
        # find the username in the collection
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get("username").lower()}
            )
        # if the username exists, check if the hash passwords match 
        if existing_user:
            if check_password_hash(
                    # compare the collection's password to the form passwords
                    existing_user["password"], request.form.get("password")):
                    # If the passwords match return a welcome message and redirect the user to the home page 
                    # create a session cookie for that user
                    session["user"] = request.form.get('username').lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for('home', username=session["user"]))
            # If the password does not match return a flash message
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        # If the username does not exist return a flash message
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    # If a user clicks the link in ANY nav bar they will be directed to the login page
    return render_template("login.html")


# logout app route
@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return render_template("index.html")


# home app route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        flash("Thank you for messaging us! We will be in touch shortly.")
        return render_template("index.html")

    if "user" in session:
        username = session["user"]

    return render_template("index.html")


# about app route
@app.route("/about")
def about():
    return render_template("about.html")


# appliance app route
@app.route("/appliance")
def appliance():
    data = mongo.db.appliances.find()
    return render_template("appliance.html", appliances=data)


# share app route
@app.route("/share", methods=["GET", "POST"])
def share():
    # check if user in session for brute-forcing
    if "user" in session:
        categories = mongo.db.category.find().sort("category_name", 1)
        types = mongo.db.type.find().sort("type_name", 1)
        if request.method == "POST":
            recipe = {
                    "recipe_name": request.form.get("recipe_name"),
                    "type": request.form.get("type"),
                    "category": request.form.get("category"),
                    "instructions": request.form.getlist("instructions"),
                    "ingredients": request.form.getlist("ingredients"),
                    "photo": request.form.get("photo"),
                    "author": session["user"]
                }
            new_recipe = mongo.db.recipes.insert_one(recipe)
            recipe_id = new_recipe.inserted_id
            flash("Thanks for sharing your recipe.")
            return redirect(url_for('recipe', recipe_id=recipe_id))

        return render_template(
            "share.html", categories=categories, types=types)

    flash("You must be logged in to acces this page!")
    return redirect(url_for("login"))


# find app route
@app.route("/find")
def find():
    recipes = mongo.db.recipes.find()
    return render_template("find.html", recipes=recipes)


# recipe app route
@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=recipe)


# update app route
@app.route('/update/<recipe_id>', methods=["GET", "POST"])
def update(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    author = recipe["author"]
    # if user in session, and session["user"] == recipe.author
    if "user" in session:
        if author.lower() == session["user"].lower():
            if request.method == "POST":
                submission = {
                    "recipe_name": request.form.get("recipe_name"),
                    "category": request.form.get("category"),
                    "type": request.form.get("type"),
                    "instructions": request.form.getlist("instructions"),
                    "ingredients": request.form.getlist("ingredients"),
                    "photo": request.form.get("photo"),
                    "author": session["user"]
                }
                mongo.db.recipes.update(
                    {"_id": ObjectId(recipe_id)}, submission)
                recipe = mongo.db.recipes.find_one(
                    {"_id": ObjectId(recipe_id)})
                flash("Recipe Updated.")
                return redirect(url_for("recipe", recipe_id=recipe_id))

            update = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
            categories = mongo.db.category.find().sort("category_name", 1)
            types = mongo.db.type.find().sort("type_name", 1)
            all_ingredients = range(0, len(update['ingredients']))
            all_instructions = range(0, len(update['instructions']))
            return render_template(
                "update.html",
                recipe=update,
                categories=categories,
                types=types,
                all_ingredients=all_ingredients,
                all_instructions=all_instructions)
    return redirect(url_for("recipe", recipe_id=recipe_id))


# delete app route
@app.route("/delete/<recipe_id>")
def delete(recipe_id):
    # if user in session, and session["user"] == recipe.author
    if "user" in session:
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        author = recipe["author"]
        if author.lower() == session["user"].lower():
            mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
            flash("Recipe Successfully deleted.")
            return redirect(url_for("find"))
        flash("You do not have permission to delete this recipe.")
        return redirect(url_for("find"))
    return redirect(url_for("find"))


# search app route
@app.route('/search', methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("find.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
