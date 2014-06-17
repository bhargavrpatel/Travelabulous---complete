var questionArray = [];
var optionsArray =[];
var answersArray = [];
var currentIndex = 0;
var doneQuestionnaire = false;

function fillOptions(option, boolx){
  if (boolx == true) {
    optionsArray.push(option);
  } else {
    optionsArray.push(option);
  }
}

function fillQuestions(question) {
    var innerArray = [];
    innerArray.push(question);
    innerArray.push(optionsArray);
    questionArray.push(innerArray);
}


function collectAnswers(leftSelected) {
    if (leftSelected) {
      answersArray[currentIndex] = 1;
    } else {
      answersArray[currentIndex] = 2;
    }

    if ((currentIndex+1) < questionArray.length) {
      currentIndex += 1;
    } else {
      doneQuestionnaire = true;
    }
}
