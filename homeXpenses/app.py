from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app) # REST api
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


def api_expenses_list():
    pass

class ApiExpensesList(Resource):
    def get(self):
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
        return expenses_list, 200
    
@app.route('/add', methods=['GET', 'POST'])
def test_add():
    expense = Expense(name="chleb", price="23", category="Jedzenia")
    db.session.add(expense)
    db.session.commit()
    return 'Added'

api.add_resource(ApiExpensesList, '/expenses_list', endpoint='expenses_list')


if __name__ == '__main__':
    # run app
    app.run()