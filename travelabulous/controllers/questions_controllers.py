from flask import Flask, render_template, request
from flask.ext.mongoalchemy import *

from travelabulous import *


@app.route('/questionnaire', methods=['POST', 'GET'])
def questionsMethod():
  if request.method == 'POST':
    user = User.query.filter(User.username == 'Guest').first()
    req = request.get_json()
    print "Success. POST recieved.\n" + "request type: " + str(type(req)) + " request content: " + str(req)
    print req['answersArray']
    print "Adding answersArray to user"
    user.options = req['answersArray']
    print "User: " + str(user) + " now has answersArray: " + str(user.options)
    return render_template('doneQuestionnaire.html', user=user.options)
  else:
    questions = session.query(Question)
  return render_template('questionnaire.html', questions=questions)
