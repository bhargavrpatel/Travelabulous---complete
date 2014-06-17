var questionArray = [];
var optionsArray = [];
var answersArray = [];
var currentIndex = 0;
var doneQuestionnaire = false;

function fillOptions(option){
  optionsArray.push(option);
}

function newArray() {
  var internalArray = [];
  if (optionsArray.length == 2) {
    internalArray = optionsArray.slice(0);
    optionsArray = [];
    return internalArray;
  }
}

function fillQuestions(question) {
    var innerArray = [];
    innerArray.push(question);
    innerArray.push(newArray());
    questionArray.push(innerArray);
}


function collectAnswers(number) {
    answersArray[currentIndex] = number;

    if ((currentIndex+1) < questionArray.length) {
      currentIndex += 1;
      rendering();
    } else {
      doneQuestionnaire = true;
      rendering();
    }
}
