from enum import unique
from pickle import FALSE
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from models import Product, db

# Init app
app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init ma
ma = Marshmallow(app)



@app.route('/', methods=['GET'])
def get():
    products = Product.query.all()
    return jsonify(products)

# Run server
if __name__ == '__main__':
    app.run(debug=True)