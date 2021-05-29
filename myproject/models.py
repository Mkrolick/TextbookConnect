from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()


# The user_loader decorator allows flask-login to load the current user
# and grab their id.
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
    phoneNumber = db.Column(db.String(128))
    location = db.Column(db.String(128))

    def __init__(self, email, username, password, permission_level, tables_created):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.permission_level = permission_level
        self.tables_created = tables_created

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class Classes(db.Model):
    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique=True, index=True)
    books = db.Column(db.PickleType)

    def __init__(self, name, books):
        self.name = name
        self.books = books


class Books(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique=True, index=True)

    def __init__(self, name, catagory, whatClasses):
        self.name = name

class Offers(db.Model):
    __tablename__ = 'offers'
    id = db.Column(db.Integer, primary_key = True)
    bookId =  db.Column(db.Integer, primary_key = True)
    sellerId = db.Column(db.Integer, primary_key = True)
