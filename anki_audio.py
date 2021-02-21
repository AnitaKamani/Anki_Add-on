# # import the main window object (mw) from aqt
# from aqt import mw
# # import the "show info" tool from utils.py
# from aqt.utils import showInfo
# # import all of the Qt GUI library
# from aqt.qt import *
#
#
# # We're going to add a menu item below. First we want to create a function to
# # be called when the menu item is activated.

# add audio
# add this to the menu gear
# if card type="German Vocabulary"
# article = "der"
# german = "Tepisch"
# sentence = "der Tepisch ist schon"
# thing="Noun_Article"+" "+"German"+"."+German_Example_Sentence
# write thing:German_Audio
import file_job
import google


def make_text(article, german, sentence):
    text = article + " " + german + ". " + sentence
    while text.find("  ") != -1:
        text = text.replace("  ", " ")
    return text


article = "der"
german = "Aufzug"
sentence = "Der Aufzug steckt fest"


text = make_text(article, german, sentence)
path = file_job.path_cache(text)
google.run(text, path)


