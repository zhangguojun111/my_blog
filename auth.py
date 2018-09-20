"""
处理登录验证等
"""

from flask import Blueprint, render_template, session, redirect
from functools import wraps
bp = Blueprint('auth', __name__)


@bp.route('/login/')
def login():
    session['user'] = 'admin'
    return redirect('/')


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

