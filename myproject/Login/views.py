from myproject import db
from flask import render_template, redirect, request, url_for, flash, Blueprint
from flask_login import login_user,login_required,logout_user
from myproject.models import User
from myproject.Login.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash



login_blueprint = Blueprint('Login', __name__, template_folder='templates/Login')



@login_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))


@login_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data,
                    phoneNumber=form.phoneNumber.data,
                    permission_level=0,
                    tables_created = 0)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('Login.login'))
    return render_template('register.html', form=form)

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not
        if user != None:
            if user.check_password(form.password.data):
                #Log in the user

                login_user(user)
                flash('Logged in successfully.')

                # If a user was trying to visit a page that requires a login
                # flask saves that URL as 'next'.
                next = request.args.get('next')

                # So let's now check if that next exists, otherwise we'll go to
                # the welcome page.
                if next == None or not next[0]=='/':
                    next = url_for('Home')

                return redirect(next)
        flash("Incorrect username or password")
    return render_template('login.html', form=form)
