from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.config['SECRET_KEY'] = '_14df1c94fe5047826a90cd663725c2f1_'
app.config['SQLALCHEMY_DATBASE_URI'] = "sqlite:////Users/ak352/Desktop/first_app/firstapp/site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from firstapp import routes
