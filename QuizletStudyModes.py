import anki

class Quizlet:
    def __init__(self):
        # initialize the flashcards and set up any necessary data structures
        self.flashcards = []
        self.current_card = 0

    def flashcards_mode(self):
        # show the flashcards one at a time and allow the user to flip through them
        self.show_flashcard()

    def learn_mode(self):
        # show the flashcards one at a time and ask the user to provide the correct answer
        self.show_flashcard()

    def spell_mode(self):
        # show a word and ask the user to type the correct spelling
        word = self.flashcards[self.current_card].prompt
        user_spelling = input("Please spell the word: " + word + ": ")

        # check the user's spelling
        if user_spelling == word:
            # the spelling is correct, mark the flashcard as correct and move on to the next one
            self.flashcards[self.current_card].mark_correct()
            self.current_card += 1

            if self.current_card < len(self.flashcards):
                # there are more flashcards to study, show the next one
                self.spell_mode()
            else:
                # all flashcards have been studied, show the summary and allow the user to review or exit
                self.show_summary()
        else:
            # the spelling is incorrect, mark the flashcard as incorrect and allow the user to try again
            self.flashcards[self.current_card].mark_incorrect()
            self.spell_mode()

    def test_mode(self):
        # show a multiple-choice question based on the flashcard and ask the user to choose the correct answer
        card = self.flashcards[self.current_card]
        print("Question: " + card.prompt)
        print("A) " + card.choices[0])
        print("B) " + card.choices[1])
        print("C) " + card.choices[2])
        print("D) " + card.choices[3])

        user_answer = input("Please choose the correct answer: ")

        # check the user's answer
        if user_answer == card.answer:
            # the answer is correct, mark the flashcard as correct and move on to the next one
            card.mark_correct()
            self.current_card += 1

            if self.current_card < len(self.flashcards):
                # there are more flashcards to study, show the next one
                self.test_mode()
            else:
                # all flashcards have been studied, show the summary and allow the user to review or exit
                self.show_summary()
        else:
            # the answer is incorrect, mark the flashcard as incorrect and allow the user to try again
            card.mark_incorrect()
            self.test_mode()

    def match_mode(self):
    # show a term and ask the user to type the corresponding definition
    term = self.flashcards[self.current_card].prompt
    user_definition = input("Please type the definition for the term: " + term + ": ")

    # check the user's definition
    if user_definition == self.flashcards[self.current_card].answer:
        # the definition is correct, mark the flashcard as correct and move on to the next one
        self.flashcards[self.current_card].mark_correct()
        self.current_card += 1

        if self.current_card < len(self.flashcards):
            # there are more flashcards to study, show the next one
            self.match_mode()
        else:
            # all flashcards have been studied, show the summary and allow the user to review or exit
            self.show_summary()
    else:
        # the definition is incorrect, mark the flashcard as incorrect and allow the user to try again
        self.flashcards[self.current_card].mark_incorrect()
        self.match_mode()
