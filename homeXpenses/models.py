from app import db
from sqlalchemy.dialects.sqlite import DECIMAL

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)


class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Float())
    category = db.Column(db.String())

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        # repr or str?
        return f'<name: {self.name}>'
