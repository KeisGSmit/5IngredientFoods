# importing dependancies and initialising app

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


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')


mongo = PyMongo(app)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Submitting the form will check if the user exists
     If it does, then a flash message appear - try again
     else a new data entry is inserted into the collection
     A cookie will then be created for the user
     user will be redirected to the home page
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
            )
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for('home', username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    The collection is searched for a matching username
    Passwords are compared
    successful login creates a redirect and a cookie
    unsuccessful login flashes messages
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get("username").lower()}
            )
        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get('username').lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for('home', username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    """
    The session cookie is removed, flash message
    user is redirected
    """
    flash("You have been logged out")
    session.pop("user")
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def home():
    # form submission renders a flash
    if request.method == "POST":
        flash("Thank you for messaging us! We will be in touch shortly.")
        return render_template("index.html")

    if "user" in session:
        username = session["user"]
    return render_template("index.html")


@app.route("/about")
def about():
    # renders a template
    return render_template("about.html")


@app.route("/appliance")
def appliance():
    """
    searches collection for data
    data is parsed to the HTML page
    """
    data = mongo.db.appliances.find()
    return render_template("appliance.html", appliances=data)


@app.route("/share", methods=["GET", "POST"])
def share():
    """
    only users in session can access - brute force prevented
    data from categories and type collection are passed into HTML form
    on submission a document is inserted into the recipes collection
    user is redirected to that recipe's page
    """
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


@app.route("/find")
def find():
    # recipes collection is searched and parsed into the HTML
    recipes = mongo.db.recipes.find()
    return render_template("find.html", recipes=recipes)


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    # renders a template for that specific recipe by search for its ID
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=recipe)


@app.route('/update/<recipe_id>', methods=["GET", "POST"])
def update(recipe_id):
    """
    recipe is searched for by its id
    page prevents brute force entry
    old data populates the form
    on submission new data updates old data
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    author = recipe["author"]
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


@app.route("/delete/<recipe_id>")
def delete(recipe_id):
    """
    Brute force entry is prevented
    only recipe author can delete recipe
    deletes recipe by ID
    """
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


@app.route('/search', methods=["GET", "POST"])
def search():
    """
    Collection recipes is index by name
    recipe names searched for in search bar are searched for
    data is parsed back into HTML
    """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("find.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
