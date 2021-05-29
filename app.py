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


@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/admin')
@login_required
def console():
    if (current_user.permission_level == 4):
        return render_template('admin.html', Users=User.query.all())
    else:
        return redirect(url_for('home'))

@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.json)
    return Response(status=200)

@app.route('/plans')
def plans():
    return render_template('plans.html')





if __name__ == '__main__':
    app.run(debug=True)
