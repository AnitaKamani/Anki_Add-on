from . import google
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from . import file_job


def make_text(article, german, sentence):
    text = article + " " + german + ". " + sentence
    while text.find("  ") != -1:
        text = text.replace("  ", " ")
    return text


def testFunction():
    deck_name = "1111::1Audio"
    did = mw.col.decks.id(deck_name)
    type_id = mw.col.backend.get_notetype_id_by_name("German Vocabulary")
    cids = mw.col.decks.cids(did, children=True)
    i = 0
    try:
        for cid in cids:
            card = mw.col.getCard(cid)
            card_type = card.note().mid
            if type_id == card_type:
                note = card.note()
                fields = note.values()
                article = fields[5]
                german = fields[0]
                sentence = fields[2]
                text = make_text(article, german, sentence)
                try:
                    file_name = file_job.file_name_creator(text)
                    path = file_job.path_cache(file_name)
                    google.run(text, path)
                    file_name = mw.col.media.addFile(path)
                    file_name = "[sound:" + file_name + "]"
                    fields[4] = file_name
                    note.flush()
                    i += 1
                except:
                    showInfo("error %d"%text)
    except:
        showInfo("error")

    showInfo("OK ;) \n\n %d cards downloaded" % i)


action = QAction("Audio Add-on", mw)
file_job.empty_cache()
action.triggered.connect(testFunction)
mw.form.menuTools.addAction(action)

