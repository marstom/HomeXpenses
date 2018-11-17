from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

@app.route('/', methods=['GET', 'POST'])
def index():
    # add new expense
    # qu = db.session.query(Expense).order_by(Expense.id)
    qu = Expense.query.all()
    expenses_list = []
    for el in qu:
        print(el.name, el.category, el.price)
        expenses_list.append(
            {
                'name': el.name,
                'price': el.price,
                'category': el.category
            }
        )
    
    return f'Hello world {expenses_list}'

@app.route('/add', methods=['GET', 'POST'])
def test_add():
    expense = Expense(name="chleb", price="23", category="Jedzenia")
    db.session.add(expense)
    db.session.commit()
    return 'Added'


if __name__ == '__main__':
    # run app
    app.run()