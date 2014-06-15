# __init__ in controllers
from travelabulous import *
import questions_controllers


@app.route("/")
def default():
  return "Hello world! from controller __init__"
