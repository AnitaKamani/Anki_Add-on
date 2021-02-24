# import the main window object (mw) from aqt
from . import google
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
from . import file_job


# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.
def make_text(article, german, sentence):
    text = article + " " + german + ". " + sentence
    while text.find("  ") != -1:
        text = text.replace("  ", " ")
    return text


def testFunction():
    # get the number of cards in the current collection, which is stored in
    # the main window
    # cardCount = mw.col.cardCount()
    # show a message box
    deck_name = "Audio"
    did = mw.col.decks.id(deck_name)
    cids = mw.col.decks.cids(did)
    i = 0
    while i < len(cids):
        if i % 2 == 0:
            cid = cids[i]
            card = mw.col.getCard(cid)
            note = card.note()
            fields = note.values()
            article = fields[5]
            german = fields[0]
            sentence = fields[2]
            text = make_text(article, german, sentence)
            file_name = file_job.file_name_creator(text)
            path = file_job.path_cache(file_name)
            google.run(text, path)
            file_name = mw.col.media.addFile(path)
            file_name = "[sound:" + file_name + "]"
            fields[4] = file_name
            note.flush()

        i += 1

    showInfo("OK ;)")


# create a new menu item, "test"
action = QAction("Audio Add-on", mw)
file_job.empty_cache()
# set it to call testFunction when it's clicked
action.triggered.connect(testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
