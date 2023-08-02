import quiz from './linked_quizdata.js'; // Replace the correct path to quizData.js

let currentQuestionIndex = 0;

// Function to shuffle an array using the Fisher-Yates algorithm
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

// Function to display the current question
function displayQuestion() {
  const currentQuestion = quiz[currentQuestionIndex];
  const questionElement = document.getElementById("question");
  const optionsElement = document.getElementById("options");

  questionElement.textContent = currentQuestion.question;
  optionsElement.innerHTML = "";

  currentQuestion.options.forEach((option, index) => {
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

// Function to check the answer and move to the next question
function checkAnswer() {
  const selectedOption = document.querySelector('input[name="option"]:checked');

  if (!selectedOption) {
    alert("Please select an option.");
    return;
  }

  const answer = selectedOption.value;
  const currentQuestion = quiz[currentQuestionIndex];
  if (answer === currentQuestion.answer) {
    // Handle the correct answer here (e.g., increment score)
  }

  currentQuestionIndex++;

  if (currentQuestionIndex < quiz.length) {
    displayQuestion();
  } else {
    displayResult();
  }
}

// Function to display the final result
function displayResult() {
  const resultElement = document.getElementById("result");
  const score = 0; // Calculate the score based on the correct answers
  resultElement.textContent = `Your score: ${score} out of ${quiz.length}`;
}

// Shuffle the quiz array before displaying the questions
shuffleArray(quiz);

// Get the submit button and attach the checkAnswer function to it
const submitButton = document.getElementById("submitBtn");
submitButton.addEventListener("click", checkAnswer);

// Display the first question when the page loads
displayQuestion();
