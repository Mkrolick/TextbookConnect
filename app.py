from myproject import app,db
from flask import render_template, redirect, request, url_for, flash,abort, Response
from flask_login import login_user,login_required,logout_user, current_user
from myproject.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from myproject.Login.forms import LoginForm
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/view_book')
@login_required
def welcome_user():
    return render_template('book_listings.html')





if __name__ == '__main__':
    app.run(debug=True)
