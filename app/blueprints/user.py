from flask import Blueprint, request, render_template, redirect,url_for
from app.models.user import User as UserModel
from app.extentions import db

bp = Blueprint("app", __name__)

@bp.route("/user/")
def all_user():
    users = UserModel.query.all()
    return render_template("user/all_users.html", users=users)

@bp.route("/user/", methods=["POST"])
def createuser():
    newUser = UserModel(
        fname = request.form["name"],
        email = request.form["email"]
    )

    db.session.add(newUser)
    db.session.commit()
    
    return redirect(url_for("app.all_user"))
    

@bp.route("/user/create")
def create():
    #return url_for("app.create")
    return render_template("user/createuser.html")

@bp.route("/user/<int:id>", methods=['DELETE', 'PUT'])
def user_id(id):
    if request.method == 'DELETE':
        user = UserModel.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return "Deleted"
    elif request.method == 'PUT':
        return "<h1> Update User!!! </h1>"
    
@bp.route("/user/<int:id>")
def about(id):
    return render_template("user/show.html", id=id)