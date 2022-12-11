# import the main window object (mw) from aqt
from aqt import mw
# import the Qt GUI library
from aqt.qt import *

def createWrittenAnswerCard() -> None:
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
note.fields["Answer"] = correctAnswerField.text()
# add the note to the collection
mw.col.addNote(note)

# create a new Card object
card = Card()
# set the card's question and answer
card.q = "{Question}"
card.a = "{Answer}"
# add the card to the note
note.addCard(card)

# create a new menu item
action = QAction("Create written answer card", mw)
# set it to call createWrittenAnswerCard when it's clicked
action.triggered.connect(createWrittenAnswerCard)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
