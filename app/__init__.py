from app.blueprints import home, user
from flask import Flask
from app.extentions import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


app.register_blueprint(home.bp)
app.register_blueprint(user.bp)

with app.app_context():
    db.create_all()