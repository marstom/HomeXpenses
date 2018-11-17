from app import db
from sqlalchemy.dialects.sqlite import DECIMAL


class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.String())
    category = db.Column(db.String())

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        # repr or str?
        return f'<name: {self.name}>'