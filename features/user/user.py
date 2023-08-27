###############################
### Dianyi Jiang            ###
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

user = Blueprint("user", __name__, template_folder="templates")

@user.route("/dashboard")
@user_login_required
def dashboard():
    currentUser = current_user()
    name = currentUser.name
    return render_template(f"user_dashboard.html", name=name)
