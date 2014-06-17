from flask import Flask
from travelabulous import app, db, session
from flask.ext.mongoalchemy import *

import Option
import Question

class User(db.Document):
  username = db.StringField(required = True)
  options = db.ListField(db.IntField(), required = False)

  def __unicode__(self):
    return self.username
  def __str__(self):
    return unicode(self).encode('utf-8')

  def __repr__(self):
    return self.username
