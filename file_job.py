"""
Path and directory initialization
"""

import os

addon = os.path.dirname(os.path.abspath(__file__))
cache = os.path.join(addon, '.cache')
path = os.path.join(cache, 'mine.mp3')
print('h\n',path)
