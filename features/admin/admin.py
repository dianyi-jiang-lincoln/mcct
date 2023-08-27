###############################
### Dianyi Jiang            ###
###############################

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from common.login_required import admin_login_required
from db import db
from common.user import *
import features.staff.query as query

admin = Blueprint("admin", __name__, template_folder="templates")

@admin.route("/dashboard")
# @admin_login_required
def dashboard():
    return render_template(f"admin_dashboard.html")
