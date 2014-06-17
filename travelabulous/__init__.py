# Main App

from flask import Flask, render_template
from flask.ext.mongoalchemy import MongoAlchemy
from mongoalchemy.session import Session

# Setup "app" as per Flask.
app = Flask(__name__, template_folder = "templates", static_folder = "assets")
app.config['MONGOALCHEMY_DATABASE'] = 'travelabulous'

# Database hook up and session creation
db = MongoAlchemy(app)
session = Session.connect('travelabulous')


from travelabulous.models import *
from travelabulous.controllers import *
from test import *
