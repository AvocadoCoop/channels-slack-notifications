from django.core.exceptions import ImproperlyConfigured

from .backends import get_backend
from .conf import app_settings


if app_settings.TOKEN is None:
    raise ImproperlyConfigured('CHANNELS_SLACK_TOKEN is required.')


def handle_notification(message):
    backend = get_backend()
    endpoint_url = app_settings.ENDPOINT_URL

    slack_data = dict(
        token = app_settings.TOKEN,
        channel = app_settings.CHANNEL,
        icon_emoji = app_settings.ICON_EMOJI,
        username = app_settings.USERNAME,
        as_user = False,
    )

    slack_data.update(message.data)

    backend(slack_data, endpoint_url)
