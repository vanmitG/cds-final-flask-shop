from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from src import db


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), index=True, unique=True)
    user_name = db.Column(db.String(80), default="User")
    password_hash = db.Column(db.String(128), nullable=False)
    img_url = db.Column(
        db.String(128), default="https://randomuser.me/api/portraits/men/77.jpg")
    events = db.relationship("Events", backref="users", lazy="dynamic")
    # comments = db.relationship("Comments", backref="users", lazy="dynamic")
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    updated_date = db.Column(
        db.DateTime,  nullable=False, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"{self.id} user_name is {self.user_name}."


class AuthModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('user.login'))


# Users Class/Model
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), index=True, unique=True)
    user_name = db.Column(db.String(80), default="User")
    password_hash = db.Column(db.String(128), nullable=False)
    img_url = db.Column(db.String(128), default="images/team/a2.png")
    posts = db.relationship("Posts", backref="users", lazy="dynamic")
    comments = db.relationship("Comments", backref="users", lazy="dynamic")
    created_date = db.Column(db.DateTime, default=datetime.now)
    updated_date = db.Column(db.DateTime, default=datetime.now)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<User %r>' % self.email

# Product Class/Model


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"product {self.id} - {self.name}."
