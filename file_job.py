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


def file_name_creator(text, svc_id="google"):
    hash_input = text

    from hashlib import sha1

    hex_digest = sha1(
        hash_input.encode('utf-8') if isinstance(hash_input, str)
        else hash_input
    ).hexdigest().lower()

    assert len(hex_digest) == 40, "unexpected output from hash library"
    file_name = '.'.join(['-'.join([
        svc_id, hex_digest[:8], hex_digest[8:16],
        hex_digest[16:24], hex_digest[24:32], hex_digest[32:],
    ]),
        'mp3'
    ])
    return file_name


def path_cache(file_name):
    return os.path.join(cache, file_name, )


def empty_cache():
    import shutil
    try:
        shutil.rmtree(cache)
    except OSError:
        pass
    try:
        os.mkdir(cache)
    except OSError:
        pass
