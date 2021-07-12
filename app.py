import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session,url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def go_homepage():
    return render_template("home.html")


@app.route("/skills")
def get_skills():
    languages = mongo.db.languages.find()
    libraries = mongo.db.libraries.find()
    frameworks = mongo.db.frameworks.find()

    return render_template("skills.html", languages=languages, libraries=libraries, frameworks=frameworks)


@app.route("/work-experience")
def get_work_experience():
    work_experience = mongo.db.work_experience.find()

    return render_template("work-experience.html", work_experience=work_experience)


@app.route("/education")
def get_education():
    education = mongo.db.education.find()

    return render_template("education.html", education=education)


@app.route("/portfolio")
def get_portfolio():
    portfolio = mongo.db.education.find()

    return render_template("portfolio.html", portfolio=portfolio)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True)