from flask import Flask, render_template
from flask.ext.mongoalchemy import *

from travelabulous import *


# @app.route('/questionnaire')
# def questionsMethod():
#   questions = session.query(Question)
#   # return render_template('hello.html')
#   return render_template('questionnaire.html', questions=questions)
