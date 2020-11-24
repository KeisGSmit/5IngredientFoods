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


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/appliance")
def appliance():
    data = []
    with open("data/appliances.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("appliance.html", appliances=data)


@app.route("/share")
def share():
    categories = mongo.db.category.find().sort("category_name", 1)
    types = mongo.db.type.find().sort("type_name", 1)
    return render_template("share.html", categories=categories, types=types)


@app.route("/find")
def find():
    return render_template("find.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
