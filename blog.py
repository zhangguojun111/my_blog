
from flask import Blueprint, render_template

bp = Blueprint('blog', __name__)




@bp.route("/tags/<keyword>/")
def tags(keyword):
    return render_template('tags.html', keyword=keyword)


@bp.route("/post/<post_path>/")
def post(post_path):
    return render_template('post.html', post_path= post_path)
    pass