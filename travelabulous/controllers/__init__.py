# __init__ in controllers
from flask import Flask, render_template
from travelabulous import *
import questions_controllers


@app.route("/")
def default():
  return "Hello world! from controller __init__"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
  return render_template('hello.html', name=name)

@app.route('/questionnaire')
def questionsMethod():
  questions = session.query(Question)
  # return render_template('hello.html')
  return render_template('questionnaire.html', questions=questions)
