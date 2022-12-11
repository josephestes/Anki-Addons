import anki

class QuizletLearn:
    def __init__(self):
        # initialize the flashcards and set up any necessary data structures
        self.flashcards = []
        self.current_card = 0

    def start_study_mode(self):
        # show the first flashcard to the user
        self.show_flashcard()

    def show_flashcard(self):
        # display the current flashcard and allow the user to provide an answer
        card = self.flashcards[self.current_card]
        user_answer = input(card.prompt + ": ")

        # check the user's answer
        if user_answer == card.answer:
            # the answer is correct, mark the flashcard as correct and move on to the next one
            card.mark_correct()
            self.current_card += 1

            if self.current_card < len(self.flashcards):
                # there are more flashcards to study, show the next one
                self.show_flashcard()
            else:
                # all flashcards have been studied, show the summary and allow the user to review or exit
                self.show_summary()
        else:
            # the answer is incorrect, mark the flashcard as incorrect and allow the user to try again
            card.mark_incorrect()
            self.show_flashcard()

    def show_summary(self):
        # show a summary of the user's performance and allow them to review or exit
        print("Study complete! Here is your summary:")
        print("Correct answers:", self.num_correct_answers())
        print("Incorrect answers:", self.num_incorrect_answers())

        review = input("Would you like to review the flashcards (Y/N)? ")
        if review.lower() == "y":
            # the user wants to review, start the study mode again
            self.current_card = 0
            self.start_study_mode()
        else:
            # the user does not want to review, exit the study mode
            print("Exiting study mode.")

# create an instance of the QuizletLearn class and start the study mode
quizlet_learn = QuizletLearn()
quizlet_learn.start_study_mode()
