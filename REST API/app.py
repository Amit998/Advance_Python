import re
from flask import Flask,request,jsonify,json
from flask.signals import request_started
from flask_sqlalchemy import SQLAlchemy

import requests
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db=SQLAlchemy(app)

class Drink(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    desc=db.Column(db.String(120))


    def __repr__(self):
        return f"{self.name} - {self.desc}"




@app.route("/")
def index():
    return "Hello World!"

@app.route('/drinks')
def get_drinks():
    drinks=Drink.query.all()
    output=[]
    for drink in drinks:
        drink_data={"name":drink.name,'desc':drink.desc}
        output.append(drink_data)
    return {"drinks":output}

@app.route('/drink/<id>')
def get_drink(id):
    drink=Drink.query.get_or_404(id)
    
    return {"name":drink.name,"desc":drink.desc}


@app.route('/drinks',methods=['POST'])
def add_drink():


    drink=Drink(id=request.args.get('id'),name=request.args.get('name'),desc=request.args.get('desc'))
    db.session.add(drink)
    db.session.commit()
    
    return {"msg":"successs"}


@app.route('/drinks/<id>',methods=['DELETE'])
def delete_drink(id):


    drink=Drink.query.get(id)

    if drink == None:
        return {"msg":"No Data"}
    db.session.delete(drink)
    db.session.commit()
    
    return {"msg":"successs"}

if __name__ == '__main__':
    app.run(debug=True)