var questionArray = [];
var optionsArray =[];

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
