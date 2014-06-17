from flask import Flask, render_template, request
from flask.ext.mongoalchemy import *

from travelabulous import *


@app.route('/questionnaire', methods=['POST', 'GET'])
def questionsMethod():
  if request.method == 'POST':
    user = User.query.filter(User.username == 'Guest').first()
    req = request.get_json()
    print "Success. POST recieved."
    print type(req)
    print req
    print req['answersArray']
    return render_template('doneQuestionnaire.html', user=req['answersArray'])
    # print user
    # answersArray = request.args.get("answersArray")
    # print answersArray
    # user.options = answersArray
    # return render_template('doneQuestionnaire.html', user=answersArray)
  else:
    questions = session.query(Question)
  return render_template('questionnaire.html', questions=questions)
