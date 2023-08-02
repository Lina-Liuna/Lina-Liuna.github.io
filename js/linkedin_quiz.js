import quiz from './linked_quizdata.js'; // Replace the correct path to quizData.js

// Rest of your quiz logic here...


const questionElement = document.getElementById("question");
const optionsElement = document.getElementById("options");
const submitButton = document.getElementById("submitBtn");
const resultElement = document.getElementById("result");

let currentQuestionIndex = 0;
let score = 0;

function displayQuestion() {
  const currentQuestion = quiz[currentQuestionIndex];
  questionElement.textContent = currentQuestion.question;
  optionsElement.innerHTML = "";

  currentQuestion.options.forEach((option) => {
    const input = document.createElement("input");
    input.type = "radio";
    input.name = "option";
    input.value = option;
    optionsElement.appendChild(input);

    const label = document.createElement("label");
    label.textContent = option;
    optionsElement.appendChild(label);

    optionsElement.appendChild(document.createElement("br"));
  });
}

function checkAnswer() {
  const selectedOption = document.querySelector('input[name="option"]:checked');

  if (!selectedOption) {
    alert("Please select an option.");
    return;
  }

  const answer = selectedOption.value;
  const currentQuestion = quiz[currentQuestionIndex];
  if (answer === currentQuestion.answer) {
    score++;
  }

  currentQuestionIndex++;

  if (currentQuestionIndex < quiz.length) {
    displayQuestion();
  } else {
    displayResult();
  }
}

function displayResult() {
  quiz.innerHTML = "";
  resultElement.style.display = "block";
  resultElement.textContent = `You scored ${score} out of ${quiz.length}.`;
}

submitButton.addEventListener("click", checkAnswer);

// Display the first question when the page loads
displayQuestion();
checkAnswer();
displayResult();
