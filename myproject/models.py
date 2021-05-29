from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    permission_level = db.Column(db.Integer)
    tables_created = db.Column(db.Integer)

    def __init__(self, email, username, password, permission_level, tables_created):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.permission_level = permission_level
        self.tables_created = tables_created

    def check_password(self,password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.password_hash,password)

class Table_Registry(db.Model):
    __tablename__ = 'table_registry'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index=True)
    owner = db.Column(db.String(64), index=True)
    q1 = db.Column(db.Boolean)
    q2 = db.Column(db.Boolean)
    q3 = db.Column(db.Boolean)
    q4 = db.Column(db.Boolean)
    q5 = db.Column(db.Boolean)
    q6 = db.Column(db.Boolean)
    q7 = db.Column(db.Boolean)
    q8 = db.Column(db.Boolean)
    q9 = db.Column(db.Boolean)
    type_page = db.Column(db.String(64)) # 3 Types Meme, Theme, Personal
    type_q1 = db.Column(db.Boolean) # Question changes upon type_page. 3 variations
    type_q2 = db.Column(db.Boolean) # Question changes upon type_page. 3 variations
    type_q3 = db.Column(db.Boolean) # Question changes upon type_page. 3 variations

    def __init__(self, name, owner, q1, q2, q3, q4, q5, q6, q7, q8, q9, type_page, type_q1, type_q2, type_q3):
        self.name = name
        self.owner = owner
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.type_page = type_page
        self.type_q1 = type_q1
        self.type_q2 = type_q2
        self.type_q3 = type_q3

#    def create_filename(self):
#        filename = self.owner + "-" + self.name
#        return filename
