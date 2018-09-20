"""
处理发帖等
"""
from flask import Blueprint, render_template, redirect, redirect, request
from auth import login_required

bp = Blueprint('admin', __name__)


@bp.route("/new/", methods=["POST", "GET"])
@login_required
def new_post():
    if request.method == "POST":
        mar = request.form.get("markdown")
        html = request.form.get("html")
        return mar+"---"+html 
    # return "错误了"
    return render_template('new.html')
