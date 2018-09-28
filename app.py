"""
主运行程序
"""
from flask import Flask, render_template, session, redirect, request
import blog
import auth
import admin
import db
import config

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = 'dey'
app.register_blueprint(blog.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(admin.bp)


@app.route("/")
def index():
    select_sql = "select * from posts ORDER BY id DESC"
    rows = db.query_db(select_sql)

    p = (len(rows) // 5)
    list_rows = []
    if request.args.get("p") != 0:  # 判断是不是一页
        count = p  # 要分的页数
        if len(rows) % 5 == 0:  # 判断是不是可以刚好展示完，
            for i in range(count + 1):
                rows1 = rows[i * 5:(i + 1) * 5]
                list_rows.append(rows1)

        else:
            for i in range(count + 1):
                rows1 = rows[i * 5:(i + 1) * 5]
                list_rows.append(rows1)
            list_rows.append(rows[count * 5:len(rows)])
            p = p + 2

    else:
        list_rows.append(rows)
        p = 1
        pass
    select_sql = "select DISTINCT tag_name from posts_tags"
    tag = db.query_db(select_sql)

    if request.args.get("p") != None:
        rows = list_rows[int(request.args.get("p")) - 1]
    else:
        rows = list_rows[0]

    res_dict = {
        "rows": rows,
        "tag": tag,
        "p": p,
    }
    return render_template("index.html", **res_dict)


if __name__ == '__main__':
    app.run()
