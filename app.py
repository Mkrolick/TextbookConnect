from myproject import app,db
from flask import render_template, redirect, request, url_for, flash,abort, Response
from flask_login import login_user,login_required,logout_user, current_user
from myproject.models import User, Classes, Books, Offers
from myproject.models import Classes as bb
from werkzeug.security import generate_password_hash, check_password_hash
from myproject.Login.forms import LoginForm

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form.get('Search')
    return redirect(url_for('BookSearch', bookName = projectpath))

@app.route('/create_request/<bookId>', methods=['POST'])
def create_request(bookId):
    price = request.form.get('text')
    bookwsId = int(bookId)
    newOffer = Offers( bookwsId, current_user.id , int(price))
    db.session.add(newOffer)
    db.session.commit()
    return render_template('home.html')
    # redirect(url_for('DisplayBook', bookName = book))

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
    stuff = True
    BooksQuery = Books.query.all()
    BookList = []
    for book in BooksQuery:
        if bookName in book.name:
            BookList.append(book)
    if (bookName == 'All'):
        BookList = []
        for book in Books.query.all():
            BookList.append(book)
    if (BookList == []):
        stuff = False
    return render_template('booksearch.html', BookList=BookList, stuff=stuff)

@app.route('/bookAll')
@login_required
def BookAll():
    stuff = True
    BooksQuery = Books.query.all()
    BookList = []
    for book in Books.query.all():
        BookList.append(book)
    return render_template('booksearch.html', BookList=BookList, stuff=stuff)


@app.route('/book/<bookName>')
@login_required
def DisplayBook(bookName):
    Book = Books.query.filter_by(name=bookName).first()
    OfferList = Offers.query.filter_by(bookId= Book.id).all()
    return render_template('bookpage.html', Book=Books.query.filter_by(name=bookName).first(), Offers=OfferList, User=User)

#me = bb('CS102 - Introduction to Computing Principles', [ "How to Prove It A Structured Approach" , "Code The Hidden Language of Computer Hardware and Software"])
#db.session.add(me)
#db.session.commit()

app.cli.add_command(create_tables)


if __name__ == '__main__':
    app.run(debug=False)
