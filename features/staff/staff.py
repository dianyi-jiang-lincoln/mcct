###############################
### Dianyi Jiang            ###
###############################

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from common.login_required import staff_login_required
from db import db
from common.user import *
import features.staff.query as query

staff = Blueprint("staff", __name__, template_folder="templates")

@staff.route("/dashboard")
# @staff_login_required
def dashboard():
    return render_template(f"staff_dashboard.html")
