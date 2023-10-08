###############################
### MCCT                    ###
###############################

import os.path
from pathlib import Path

from flask import Blueprint
from flask import render_template, redirect
from flask import request, flash
from flask import url_for
from flask import send_file
import sys
from common.login_required import user_login_required
from common.user import *
from db import db
import features.user.query as query

user = Blueprint(
    "user",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/user",
)


@user.route("/dashboard")
@user_login_required
def dashboard():
    currentUser = current_user()
    name = currentUser.name
    return render_template(f"user_dashboard.html", name=name)


@user.route("/home")
def home():
    return render_template(f"user_home.html")


@user.route("/aboutus")
def aboutus():
    trusteeList = db.sql_exec_with_connection(
        query=query.get_trustee(), callback=db.get_mapped_titles_rows
    )
    return render_template(f"user_aboutus.html", trusteeList=trusteeList)


@user.route("/projects")
def projects():
    return render_template(f"user_projects.html")


@user.route("/news")
def news():
    newsList = db.sql_exec_with_connection(
        query=query.get_news(), callback=db.get_mapped_titles_rows
    )

    eventList = db.sql_exec_with_connection(
        query=query.get_events(), callback=db.get_mapped_titles_rows
    )

    return render_template(f"user_news.html", newsList=newsList, eventList=eventList)
