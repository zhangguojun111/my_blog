"""
处理发帖等
"""
from flask import Blueprint, render_template,redirect
from auth import login_required

bp = Blueprint('admin', __name__)


@bp.route("/new/")
@login_required
def new_post():

    return render_template('new.html')

