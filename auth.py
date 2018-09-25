"""
处理登录验证等
"""

from flask import Blueprint, render_template, session, redirect, request
from functools import wraps
import db

bp = Blueprint('auth', __name__)


@bp.route('/login/', methods=["POST", "GET"])
def login():
    """登录"""
    if request.method == "POST":
        username = request.form.get("username")
        sql = "SELECT * FROM user WHERE name='" + username + "'"
        rows = db.query_db(sql, one=True)
        if rows[2] == request.form.get("password"):
            session['user'] = rows[0]
            return redirect('/')
        else:
            return render_template("loginfailure.html")
    else:
        return render_template("login.html")


@bp.route('/logout/')
def logout():
    del session['user']
    return redirect('/')


@bp.app_template_global()
def is_login():
    return 'user' in session


def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(**kwargs):
        if not is_login():
            return redirect('/')
        return view_func(**kwargs)

    return wrapped_view
