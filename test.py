from travelabulous import *
from travelabulous.models import *


print "Creating Sample question"
question1 = Question(
  id = 2,
  text = "Do you like clubbing or site tours",
  options = [
  Option(text="http://hqscreen.com/wallpapers/l/1280x800/59/architecture_design_bar_lighting_night_club_neon_lounge_1280x800_58044.jpg", isPicture = True, isLeft = True),
  Option(text="http://www.danielseidel.com/wp-content/uploads/2012/04/IMG_2956_blog.jpg", isPicture = True, isLeft = False)
]
)

print "Testing creation was valid..."
assert question1.id == 2;
assert question1.text == 'Do you like clubbing or site tours';
assert question1.options[1].isLeft == False

print "Testing modification of data..."
question1.text = "This would be the new question"
print "Testing if question text name was successful.."
assert question1.text == "This would be the new question"

print "Removing question from db"
question1.remove()
