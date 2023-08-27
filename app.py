###############################
### Dianyi Jiang            ###
###############################

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

import smtplib
import db.query as query
import git
import os

from features.admin.admin import admin
from features.staff.staff import staff
from features.user.user import user
from common.user import *
from ci import ci
from dotenv import load_dotenv
from db import db
from db import query

app = Flask(__name__)
app.secret_key = "secret key"
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(staff, url_prefix="/staff")
app.register_blueprint(user, url_prefix="/")

currentUser = None

@app.route("/")
def home():
    return render_template(f"index.html")

@app.route("/admin")
def admin():
    return redirect(url_for(f"admin.dashboard"))

@app.route("/staff")
def staff():
    return redirect(url_for(f"staff.dashboard"))

@app.route("/login", methods=["GET", "POST"])
def login():
    global currentUser
    if request.method == "GET":
        currentUser = None
        clear_session()
        return render_template("login.html")
    # get email and password
    email = request.form["email"].strip()
    password = request.form["password"].strip()
    params = [email]

    # privode convient port under development
    if os.getenv("ENV") == "DEVELOPMENT":
        return redirect(url_for("staff.dashboard"))
    else:
        flash(f"password is not valid, please try again.", "error")
        return render_template(f"login.html")

@app.route("/logout")
def logout():
    currentUser = None
    clear_session()
    return redirect(url_for("login"))

@app.route("/github_webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "hello"

    # x_hub_signature = request.headers.get("X-Hub-Signature")
    # if not ci.is_valid_signature(x_hub_signature, request.data, "WE32&*#hs9sf"):
    #     return "validation error", 401

    PROJECT_DIR = os.getenv("PROJECT_DIR")
    path = os.path.join(os.getcwd(), PROJECT_DIR)
    repo = git.Repo(path)
    origin = repo.remotes.origin
    origin.pull()
    return "Updated PythonAnywhere successfully", 200
