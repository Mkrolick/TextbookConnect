import click
from flask.cli import with_appcontext

from myproject import db
from myproject.models import User, Classes, Books, Offers
#from myproject.surveysparrow_api import Client


@click.command(name="create_tables")
@with_appcontext
def create_tables():
    db.create_all()

#@click.command(name="create_webhook")
#@with_appcontext
#def create_webhook():
#    Client().create_webhook()
