"""
Path and directory initialization
"""

import os

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