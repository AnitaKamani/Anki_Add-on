"""
Path and directory initialization
"""

import os

# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
# import all of the Qt GUI library
from aqt.qt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

addon = os.path.dirname(os.path.abspath(__file__))
cache = os.path.join(addon, '.cache')


def path_cache(text, svc_id="google"):
    hash_input = text

    from hashlib import sha1

    hex_digest = sha1(
        hash_input.encode('utf-8') if isinstance(hash_input, str)
        else hash_input
    ).hexdigest().lower()

    assert len(hex_digest) == 40, "unexpected output from hash library"
    return os.path.join(
        cache,
        '.'.join([
            '-'.join([
                svc_id, hex_digest[:8], hex_digest[8:16],
                hex_digest[16:24], hex_digest[24:32], hex_digest[32:],
            ]),
            'mp3',
        ]),
    )


def okay(path, deck_name="Audio"):
    filename = mw.col.media.addFile(path)

    did = mw.col.decks.id(deck_name)
    cids = mw.col.decks.cids(did)
    for cid in cids:
        card = mw.col.getCard(cid)
        card.nid

    # deck = mw.col.decks.get(did)

    # notes=deck.ge
    # note_field==note.fields

    """Count the success and update the note."""
    card = mw.col.sched.getCard()
    ids = mw.col.findCards("tag:x")

    note = self._accept_next_output(note, filename)
    note.flush()

    did = mw.col.decks.id("ImportDeck")
