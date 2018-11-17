from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_restful import Api, Resource, reqparse
import json
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app) # REST api
CORS(app)
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
                'category': el.category,
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
        """ 
        Get list of expenses
        """
        qu = Expense.query.all()
        expenses_list = []
        for el in qu:
            print(el.name, el.category, el.price)
            expenses_list.append(
                {
                'pk': el.id,
                'name': el.name,
                'price': el.price,
                'category': el.category,
                }
            )
        return expenses_list, 200
    
    def post(self):
        """
        http POST http://localhost:5000/expenses_list name="kupno ogórków" price=213 category="Jedzenie"
        """
        data = json.loads(request.data)
        new_expense = Expense(
                name=data.get('name'),
                price=data.get('price'),
                category=data.get('category'),
            )
        db.session.add(new_expense)
        db.session.commit()
        return {'message': 'successfull add expense!'}
    
    def patch(self):
        """
        Risky function, uptades all entrys in database
        http PATCH http://localhost:5000/expenses_list data="{json}"
        """
        data = json.loads(request.data)
        print(data)
        for el in data:
            expense = Expense.query.get(int(el['pk']))
            expense.name = el['name']['v']
            expense.price = el['price']['v']
            expense.category = el['price']['v']
        
        db.session.commit()
        return {'message': 'success!'}, 302
    
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
    
    def delete(self, pk):
        """
        Delete entry from table
        http DELETE http://localhost:5000/expense/3
        """
        el = Expense.query.get(pk)
        db.session.delete(el)
        db.session.commit()
        return {'message': f'Delete object with id {pk}'}

# api.add_resource(ApiExpensesList, '/expenses_list', endpoint='expenses_list')
# api.add_resource(ApiExpensesList, '/expense/<pk>', endpoint='expense')

if __name__ == '__main__':
    # run app
    app.run()