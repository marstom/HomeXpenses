from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_restful import Api, Resource, reqparse
import json


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app) # REST api
db = SQLAlchemy(app)


from models import *

@app.route('/', methods=['GET', 'POST'])
def index():
    """ only test """
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

@api.resource('/expenses_list')
class ApiExpensesList(Resource):
    def get(self):
        """ Get list of expenses """
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
    
@api.resource('/expense/<int:pk>')
class ApiExpense(Resource):
    pass
    def get(self, pk):
        el = Expense.query.get(pk)
        expense_dict = {
            'name': el.name,
            'price': el.price,
            'category': el.category,
        }
        return expense_dict, 200

    def patch(self, pk):
        """
        Test:
        http PATCH http://localhost:5000/expense/3 price=4
        """
        print(request)

        data = json.loads(request.data)
        el = Expense.query.get(pk)
        if data.get('price'):
            el.price = data.get('price')
        db.session.commit()

        expense_dict = {
            'name': el.name,
            'price': el.price,
            'category': el.category,
        }
        return expense_dict, 302

# api.add_resource(ApiExpensesList, '/expenses_list', endpoint='expenses_list')
# api.add_resource(ApiExpensesList, '/expense/<pk>', endpoint='expense')

if __name__ == '__main__':
    # run app
    app.run()