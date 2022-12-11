# Import the necessary modules from the Anki API
from aqt import mw
from aqt.utils import showInfo
from aqt.reviewer import Reviewer

# Define the test mode
def testMode(self):
    # Show a message to the user indicating that they are in test mode
    showInfo("You are now in test mode. A multiple choice quiz will be generated for you based on the terms and definitions on your flashcards.")

    # Generate the quiz questions and answers randomly using the terms and definitions from the user's flashcards
    quiz = generateQuiz(self.card.note())

    # Display the quiz to the user
    self._showQuiz(quiz)

# Add the test mode to the Reviewer class
Reviewer._testMode = testMode

# Define the function for generating the quiz
def generateQuiz(note):
    # Initialize the quiz as an empty list
    quiz = []

    # Get the terms and definitions from the note
    terms = note.fields[0]
    definitions = note.fields[1]

    # Shuffle the terms and definitions
    random.shuffle(terms)
    random.shuffle(definitions)

    # Loop through the terms and create a quiz question for each one
    for i in range(len(terms)):
        # Choose three random definitions as the answer choices for the question
        choices = random.sample(definitions, 3)

        # Add the correct answer and the choices to the quiz
        quiz.append({
            "question": terms[i],
            "answer": definitions[i],
            "choices": choices
        })

    # Return the quiz
    return quiz
