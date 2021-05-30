import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import re


local = True
# Create a login manager object
login_manager = LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))

if local:
    SQLite_Database =  'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLite_Database
else:
    try:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + re.search('(.*)://(.*)' , os.environ.get('DATABASE_URL')).group(2)
    except:
        pass
#'sqlite:///' + os.path.join(basedir, 'data.sqlite')

#Postgre_Database_URL = 'postgresql://' + re.search('(.*)://(.*)' , os.environ.get('DATABASE_URL')).group(2)




#result = re.search('(.*)://(.*)' , os.environ.get('DATABASE_URL')).group(2)
#print(result)
#"postgresql://" + result

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "Login.login"

from myproject.Login.views import login_blueprint


app.register_blueprint(login_blueprint,url_prefix="/Login")
