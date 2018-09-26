"""
处理登录，退出
"""
from flask import Blueprint, render_template
import db
bp = Blueprint('blog', __name__)


@bp.route("/tags/<keyword>/")
def tags(keyword):
    """
    展示tags 部分的内容
    :param keyword:
    :return:
    """




    select_sql = "SELECT * FROM posts WHERE id in (select post_id FROM posts_tags WHERE tag_name='"+keyword+"') ORDER BY id DESC"
    rows = db.query_db(select_sql)
    select_sql = "select DISTINCT tag_name from posts_tags"
    tag = db.query_db(select_sql)


    return render_template('tags.html', keyword=keyword,rows = rows, tag=tag)


@bp.route("/post/<post_path>/")
def post(post_path):
    """
    展示文章
    :param post_path:
    :return:
    """
    select_sql = "select * from posts where url ='"+post_path+"'"
    content = db.query_db(select_sql, one=True)


    select_sql = "select DISTINCT tag_name from posts_tags"
    tag = db.query_db(select_sql)


    return render_template('post.html', post_path=content[4], tag=tag)


@bp.route("/archives/<keyword>/")
def archives(keyword):
    """
    展示Archives部分的内容
    :param keyword:
    :return:
    """

    select_sql = "SELECT * FROM posts WHERE ceated_at > '"+keyword+"-00-00 00:00:00 ' ORDER BY id DESC"
    rows = db.query_db(select_sql)
    select_sql = "select DISTINCT tag_name from posts_tags"
    tag = db.query_db(select_sql)
    return render_template('tags.html', keyword=keyword,tag=tag, rows=rows)
