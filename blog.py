"""
处理登录，退出
"""
from flask import Blueprint, render_template

bp = Blueprint('blog', __name__)


@bp.route("/tags/<keyword>/")
def tags(keyword):
    """
    展示tags 部分的内容
    :param keyword:
    :return:
    """
    return render_template('tags.html', keyword=keyword)


@bp.route("/post/<post_path>/")
def post(post_path):
    """
    展示文章
    :param post_path:
    :return:
    """
    return render_template('post.html', post_path=post_path)


@bp.route("/archives/<keyword>/")
def archives(keyword):
    """
    展示Archives部分的内容
    :param keyword:
    :return:
    """
    return render_template('tags.html', keyword=keyword)
