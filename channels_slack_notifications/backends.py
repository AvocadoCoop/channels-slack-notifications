from __future__ import unicode_literals

import pprint

from django.utils.module_loading import import_string

import requests

from .conf import app_settings


class SlackException(ValueError):
    pass


def console(data, url):
    print("-" * 79)
    print("Slack message:")
    pprint.pprint(data, indent=4)
    print("-" * 79)


def handle_error(resp):
    if resp.headers['Content-Type'].startswith('application/json'):
        result = resp.json()

        if not result['ok']:
            raise SlackException(result['error'])

        return

    if resp.text != 'ok':
        raise SlackException(resp.text)


def default(data, url):
    resp = requests.post(url, data=data)
    handle_error(resp)


def get_backend():
    """
    Wrap the backend in a function to not load it at import time.
    get_backend() caches the backend on first call.
    """
    if get_backend.backend is None:
        get_backend.backend = import_string(app_settings.BACKEND)
    return get_backend.backend
get_backend.backend = None
