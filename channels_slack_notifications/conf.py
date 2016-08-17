from django.conf import settings


def setting(suffix, default):
    @property
    def fn(self):
        return getattr(settings, 'CHANNELS_SLACK_%s' % suffix, default)
    return fn


class AppSettings(object):
    ENDPOINT_URL = 'https://slack.com/api/chat.postMessage'
    DEFAULT_BACKEND = 'channels_slack_notifications.backends.console'

    TOKEN = setting('TOKEN', None)
    CHANNEL = setting('CHANNEL', '#general')
    USERNAME = setting('USERNAME', 'notifcationbot')
    ICON_EMOJI = setting('ICON_EMOJI', ':robot_face:')

    BACKEND = setting('BACKEND', DEFAULT_BACKEND)

app_settings = AppSettings()
