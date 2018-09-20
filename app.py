"""
主运行程序
"""
from flask import Flask, render_template,session,redirect
import blog
import auth
import admin


app = Flask(__name__)
app.secret_key = 'dey'
app.register_blueprint(blog.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(admin.bp)



@app.route("/")
def index():
    return render_template("index.html")





if __name__ == '__main__':
    app.run(debug=True)
