# Import the necessary modules from the Anki Python library
from anki.hooks import addHook
from anki.lang import _
from anki.utils import intTime
from aqt import mw
from aqt.qt import *
from aqt.studydeck import StudyDeck

# Define a new study mode that switches between multiple choice and written answers
class AdaptiveStudyMode(StudyDeck):
    def __init__(self):
        # Initialize the study mode
        super(AdaptiveStudyMode, self).__init__()

    def onStart(self):
        # Set up the study session
        self.currentQuestionIndex = 0
        self.score = 0
        self.questions = []

        # Initialize the list of questions to be presented
        self.questions = self.getQuestions()

        # Set the initial study mode to multiple choice
        self.studyMode = "multipleChoice"

    def onQuestion(self):
        # Get the current question
        currentQuestion = self.questions[self.currentQuestionIndex]

        # Present the question to the user
        if self.studyMode == "multipleChoice":
            # Present the question as a multiple choice question
            self.showQuestion(currentQuestion, currentQuestion.choices)
        else:
            # Present the question as a written answer question
            self.showQuestion(currentQuestion)

    def onAnswer(self):
        # Get the user's answer
        userAnswer = self.getUserAnswer()

        # Check if the user's answer is correct
        isCorrect = self.checkAnswer(userAnswer)

        # Update the user's score
        if isCorrect:
            self.score += 1

        # Determine whether to switch to written answers
        if self.studyMode == "multipleChoice" and self.score / self.currentQuestionIndex < 0.8:
            # Switch to written answers
            self.studyMode = "writtenAnswer"
