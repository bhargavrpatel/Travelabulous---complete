from flask import Flask
from travelabulous import app, db, session
from flask.ext.mongoalchemy import *

import Question

class Option(db.Document):
  text = db.StringField(required = True)
  isPicture = db.BoolField(required = True)
  isLeft = db.BoolField(required = False)

  def __repr__(self):
    return self.text
