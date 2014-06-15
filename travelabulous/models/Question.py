from flask import Flask
from travelabulous import app, db, session
from flask.ext.mongoalchemy import *

import Option

class Question(db.Document):
  text = db.StringField(required = True)
  options = db.ListField(db.DocumentField('Option'), required = False)

  def __unicode__(self):
    return self.text
  def __str__(self):
    return unicode(self).encode('utf-8')

  def __repr__(self):
    return "Question: " + self.text + "\nOptions: " + ', '.join(str(x) for x in self.options)


class Option(db.Document):
  text = db.StringField(required = True)
  isPictureOption = db.BoolField(required = True)

  def __unicode__(self):
    return self.text
  def __str__(self):
        return unicode(self).encode('utf-8')
