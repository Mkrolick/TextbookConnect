from myproject import app,db
from flask import render_template, redirect, request, url_for, flash,abort, Response
from flask_login import login_user,login_required,logout_user, current_user
from myproject.models import User, Classes, Books, Offers
from werkzeug.security import generate_password_hash, check_password_hash
from myproject.Login.forms import LoginForm


@app.route('/')
def Home():
    return render_template('home.html')


@app.route('/classes')
@login_required
def Classes():
    return render_template('classes.html', Classes=Classes.query.all())

@app.route('/class')
@login_required
def Class(Class):
    return render_template('class.html', Class=Class)

@app.route('/book')
@login_required
def Book(bookname):
    return render_template('bookpage.html', Book=Books.query.filter_by(name=bookname).first())




if __name__ == '__main__':
    app.run(debug=True)
