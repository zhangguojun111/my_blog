"""
主运行程序
"""
from flask import Flask, render_template,session,redirect
import blog
import auth
import admin
import db

app = Flask(__name__)
app.secret_key = 'dey'
app.register_blueprint(blog.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(admin.bp)



@app.route("/")
def index():
    select_sql = "select * from posts ORDER BY id DESC"
    rows = db.query_db(select_sql)
    select_sql = "select DISTINCT tag_name from posts_tags"
    tag = db.query_db(select_sql)

    return render_template("index.html", rows= rows,tag= tag)





if __name__ == '__main__':
    app.run(debug=True)
