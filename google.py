import requests
from anki_audio import *


def run(text, path):
    """
    Downloads from Google directly to an MP3.
    """
    try:
        return net_download(
            path,
            'https://translate.google.com/translate_tts?ie=UTF-8&ttsspeed=1.0&client=tw-ob&tl=de&q=' + text
        )
    except:
        pass


def net_download(path, link):
    """
    Downloads a file to the given path from the specified target(s).
    See net_stream() for information about available options.
    """

    payload = net_stream(link)
    return payload
    # with open(path, 'wb') as response_output:
    #     response_output.write(payload)


def net_stream(link):
    DEFAULT_TIMEOUT = 15
    method = 'GET'

    response = requests.request(
        method=method,
        url=link,
        timeout=DEFAULT_TIMEOUT,
    )
    payload = response.content
    response.close()
    return payload



