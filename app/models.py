from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), unique=False)
    last_name = db.Column(db.String(120), unique=False)
    email = db.Column(db.String(128))
    number = db.Column(db.String(64))

    def __repr__(self):
        return '<User {}>'.format(self.first_name)


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(120), unique=False)

    def __repr__(self):
        return '<Admin {}>'.format(self.admin)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))
