from myproject import app,db
from flask import render_template, redirect, request, url_for, flash,abort, Response
from flask_login import login_user,login_required,logout_user, current_user
from myproject.models import User, Classes, Books, Offers
from myproject.models import Classes as bb
from werkzeug.security import generate_password_hash, check_password_hash
from myproject.Login.forms import LoginForm


@app.route('/')
def Home():
    return render_template('home.html')


@app.route('/classes')
@login_required
def Classes():
    return render_template('classes.html', Classes=bb.query.all())

@app.route('/class/<className>')
@login_required
def ClassQuery(className):
    Class = bb.query.filter_by(name=className).first()
    Class = [Class]
    return render_template('class.html', Class=Class)

@app.route('/bookSearch/<bookName>')
@login_required
def BookSearch(bookName):
    BooksQuery = Books.query.all()
    BookList = []
    for book in BooksQuery:
        if bookName in book.name:
            BookList.append(book)
    if (bookName == 'All'):
        BookList = []
        for book in Books.query.all():
            BookList.append(book)
    return render_template('booksearch.html', BookList=BookList)

@app.route('/book/<bookName>')
@login_required
def DisplayBook(bookName):
    Book = Books.query.filter_by(name=bookName).first()
    return render_template('bookpage.html', Book=Books.query.filter_by(name=bookName).first())

#me = bb('CS102 - Introduction to Computing Principles', [ "How to Prove It A Structured Approach" , "Code The Hidden Language of Computer Hardware and Software"])
#db.session.add(me)
#db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
