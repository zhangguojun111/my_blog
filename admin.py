"""
处理发帖等
"""
from flask import Blueprint, render_template, redirect, request, session,jsonify
from auth import login_required
import db

bp = Blueprint('admin', __name__)


@bp.route("/new/", methods=["POST", "GET"])
@login_required
def new_post():
    if request.method == "POST":
        mar = request.form.get("markdown")  # 编辑元吗
        html = request.form.get("html")  # HTML 源码
        title = request.form.get("title")  # 标题
        tag = request.form.get("tag")  # 标签
        tag_list = tag.split('，')
        user_id = session['user']
        # user_id = int(user)
        # 存储 标题信息

        sql = "INSERT INTO posts(`url`, `title`, `content_text`, `content_html`,user_id) VALUES  \
               ('%s','%s','%s','%s','%d')" % (title, title, mar, html, user_id)
        db.update_db(sql)
        # 存储标签内容
        title_selectsql = "SELECT * FROM posts WHERE title='" + title + "'"
        rows = db.query_db(title_selectsql, one=True)
        for i in tag_list:
            post_tag_sql = "INSERT INTO posts_tags(post_id,tag_name) value('%d','%s')" % (rows[0], i)
            db.update_db(post_tag_sql)

        return mar + "---" + html + "---" + title + "---" + str(tag_list) + 'l:' + str(rows[0])
    # return "错误了"
    return render_template('new.html')



@bp.route("/image/", methods=["POST", "GET"])
@login_required
def image():
    image_data = request.form.data()

    d = {
    "success" : 1,
    "message": "Runoob",
    "url" : "http://www.runoob.com"
}
    data = {"success" : 1,
    "message": "Runoob",
    "url" : "http://www.runoob.com"}
    print(image_data)
    return jsonify(data)
    pass