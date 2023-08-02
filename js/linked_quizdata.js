// quizData.js
const quiz = [
  {
    question: "What cmd let you create a connection between a local and remote repository?",
    options: ["git remote add new", "git remote add origin", "git remote new origin", "git remote origin"],
    answer: "git remote add origin"
  },
  {
    question: "you current project has several branches, master, beta, and push-notificaions. You've just finished the nofication"\
    "feature in the push-notification branch, and you want to commit it to beta branch. how can you accomplish this?",
    options:["checkout the push-notifications branch and run git merge beta",
            "checkout the master branch and run git merge beta -> push-notifications",
            'delete the push-notifications branch and it will be committed to the mater branch automatically',
            'checkout the beta branch and run git merge push-notifications'
    ],
    answer: "checkout the beta branch and run git merge push-notifications"

  },
  // Add more quiz questions and answers here
];

export default quiz;
