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
    if request.method == "POST":
        # check if username already exists
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

        # put the user into the current "session" - like a cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for('home'))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({'username': request.form.get("username").lower()})
        if existing_user:
            if check_password_hash(existing_user["password"], request.form.get("password")):
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


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        flash("Thank you for messaging us! We will be in touch shortly.")
        return render_template("index.html")

    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/appliance")
def appliance():
    data = mongo.db.appliances.find()
    return render_template("appliance.html", appliances=data)


@app.route("/share", methods=["GET", "POST"])
def share():
    categories = mongo.db.category.find().sort("category_name", 1)
    types = mongo.db.type.find().sort("type_name", 1)
    if request.method == "POST":
        recipe = {
                "recipe_name": request.form.get("recipe_name"),
                "type": request.form.get("type"),
                "category": request.form.get("category"),
                "instructions": request.form.getlist("instructions"),
                "ingredients": request.form.getlist("ingredients"),
                "Photo": request.form.get("photo")
            }
        mongo.db.recipes.insert_one(recipe)
        flash("Thanks for sharing your recipe.")
        return redirect(url_for('home'))

    return render_template("share.html", categories=categories, types=types)


@app.route("/find")
def find():
    recipes = mongo.db.recipes.find()
    return render_template("find.html", recipes=recipes)


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=recipe)


@app.route('/update/<recipeId>', methods=["GET", "POST"])
def update(recipeId):
    if request.method == "POST":
        submission = {
            "recipe_name": request.form.get("recipe_name"),
            "category": request.form.get("category"),
            "type": request.form.get("type"),
            "instructions": request.form.getlist("instructions"),
            "ingredients": request.form.getlist("ingredients"),
            "Photo": request.form.get("photo")
        }
        mongo.db.recipes.update({"_id": ObjectId(recipeId)}, submission)
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipeId)})
        flash("Recipe Updated.")
        return render_template('recipe.html', recipe=recipe)

    update = mongo.db.recipes.find_one({"_id": ObjectId(recipeId)})
    categories = mongo.db.category.find().sort("category_name", 1)
    types = mongo.db.type.find().sort("type_name", 1)
    all_ingredients = range(0, len(update['ingredients']))
    all_instructions = range(0, len(update['instructions']))
    return render_template("update.html",
                            recipe=update,
                            categories=categories,
                            types=types,
                            all_ingredients=all_ingredients,
                            all_instructions=all_instructions)


@app.route("/delete/<recipe_id>")
def delete(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully deleted.")
    return redirect(url_for("find"))


@app.route('/search', methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("find.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
