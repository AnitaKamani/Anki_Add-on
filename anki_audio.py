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
from google import run


def make_text(article, german, sentence):
    text = article + " " + german + ". " + sentence
    while text.find("  ") != -1:
        text = text.replace("  ", " ")
    return text


audio=run(make_text("das","Auto","das Auto ist sehr schon"), 'dsf')
with open('myfile.wav', mode='w+b') as f:
    f.write(audio)