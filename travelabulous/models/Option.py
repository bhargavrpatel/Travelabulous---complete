from flask import Flask
from travelabulous import app, db, session
from flask.ext.mongoalchemy import *

import Question

class Option(db.Document):
  text = db.StringField(required = True)
  isPictureOption = db.BoolField(required = True)

  def __unicode__(self):
    return self.text
  def __str__(self):
        return unicode(self).encode('utf-8')
