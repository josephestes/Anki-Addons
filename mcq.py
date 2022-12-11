# import the main window object (mw) from aqt
from aqt import mw
# import the Qt GUI library
from aqt.qt import *

def createMultipleChoiceCard() -> None:
    # create the dialog box
    dialog = QDialog()
    # create a layout for the dialog box
    layout = QFormLayout()
    # add a text field for the question
    questionField = QLineEdit()
    layout.addRow("Question:", questionField)
    # add a text field for the correct answer
    correctAnswerField = QLineEdit()
    layout.addRow("Correct answer:", correctAnswerField)
    # add text fields for the incorrect answers
    incorrectAnswerFields = []
    for i in range(3):
        field = QLineEdit()
        layout.addRow("Incorrect answer %d:" % (i + 1), field)
        incorrectAnswerFields.append(field)
    # add a button to submit the answers
    button = QPushButton("Create card")
    layout.addRow(button)
    # set the layout of the dialog box
    dialog.setLayout(layout)
    # show the dialog box
    dialog.exec_()

# import the Note and Card classes
from anki.notes import Note, Card

# create a new Note object
note = Note()
# set the note's fields
note.fields["Question"] = questionField.text()
note.fields["Correct"] = correctAnswerField.text()
note.fields["Incorrect1"] = incorrectAnswerFields[0].text()
note.fields["Incorrect2"] = incorrectAnswerFields[1].text()
note.fields["Incorrect3"] = incorrectAnswerFields[2].text()
# add the note to the collection
mw.col.addNote(note)

# create a new Card object
card = Card()
# set the card's question and answer
card.q = "{Question}"
card.a = "{Correct}\n\n{Incorrect1}\n{Incorrect2}\n{Incorrect3}"
# add the card to the note
note.addCard(card)

# create a new menu item
action = QAction("Create multiple choice card", mw)
# set it to call createMultipleChoiceCard when it's clicked

action.triggered.connect(createMultipleChoiceCard)

# and add it to the tools menu

mw.form.menuTools.addAction(action)
