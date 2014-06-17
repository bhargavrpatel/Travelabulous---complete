from travelabulous import *
from travelabulous.models import *
user = User(username = "Guest", options = [])
user.save()
question1 = Question(
  id = 1,
  text = "Do you like Museums or Beaches",
  options = [
  Option(text="http://i.imgur.com/dEb6XJp.jpg", issPiscture = True, isLeft = True),
  Option(text = "http://i.imgur.com/5XEPbBB.jpg", isPicture = True, isLeft = False)
]
)
question1.save()
question2 = Question(
  id = 2,
  text = "Do you like clubbing or site tours",
  options = [
  Option(text = "http://i.imgur.com/bmYP2i6.jpg", isPicture = True, isLeft = True),
  Option(text = "http://i.imgur.com/E3jjnap.jpg", isPicture = True, isLeft = False)
]
)
question2.save()
question3 = Question(
  id = 3,
  text = "Do you like Retail malls or shopping outlets",
  options = [
  Option(text = "http://i.imgur.com/yF1qC2s.jpg", isPicture = True, isLeft = True),
  Option(text = "http://i.imgur.com/Gh9g7yX.jpg", isPicture = True, isLeft = False)
]
)
question3.save()
question4 = Question(
  id = 4,
  text = "Do you like boat tours or bus tours",
  options = [
  Option(text = "http://i.imgur.com/S9UxPUl.jpg", isPicture = True, isLeft = True),
  Option(text = "http://i.imgur.com/HPavlWA.jpg", isPicture = True, isLeft = False)
]
)
question4.save()
question5 = Question(
  id = 5,
  text = "Do you like Site tours or Adventures",
  options = [
  Option(text = "http://i.imgur.com/CifGMWR.jpg", isPicture = True, isLeft = True),
  Option(text = "http://i.imgur.com/vcV8h7B.jpg", isPicture = True, isLeft = False)
]
)
question5.save()
question6 = Question(
  id = 6,
  text = "Do you like Amusement parks or going to the Spa to relax",
  options = [
  Option(text = "http://i.imgur.com/bSEz80b.jpg", isPicture = True, isLeft = True),
  Option(text = "http://i.imgur.com/gmHKABL.jpg", isPicture = True, isLeft = False)
]
)
question6.save()
question7 = Question(
  id = 7,
  text = "Do you like Iconics or Cultural Experiences",
  options = [
  Option(text = "http://i.imgur.com/jIPds0s.jpg", isPicture = True, isLeft = True),
  Option(text = "http://i.imgur.com/WqbrgGa.jpg", isPicture = True, isLeft = False)
]
)
question7.save()
question8 = Question(
  id = 8,
  text = "Do you prefer Downtown or Rural areas",
  options = [
  Option(text = "http://i.imgur.com/sm4EbuM.jpg", isPicture = True, isLeft = True),
  Option(text = "http://i.imgur.com/Gfq1WDj.jpg", isPicture = True, isLeft = False)
]
)
question8.save()
