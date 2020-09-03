from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), unique=False)
    last_name = db.Column(db.String(120), unique=False)
    email = db.Column(db.String(128))
    number = db.Column(db.String(64))

    def __repr__(self):
        return '<User {}>'.format(self.first_name)
