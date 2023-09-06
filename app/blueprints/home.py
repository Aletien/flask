from flask import Blueprint, render_template

bp = Blueprint("home", __name__)

@bp.route("/")
def index():
    return render_template("home/home.html")

@bp.route("/contact")
def contact():
    return render_template("home/contact.html")