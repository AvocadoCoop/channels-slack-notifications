from django.core.management.base import BaseCommand

from channels_slack_notifications.backends import get_backend
from channels_slack_notifications.conf import app_settings


class Command(BaseCommand):
    help = 'Sends a test "Hello, Slack!" message to test your slack configuration'

    def handle(self, *args, **options):
        message = "Hello, Slack!"
        backend = get_backend()
        endpoint_url = app_settings.ENDPOINT_URL

        slack_data = dict(
            text = message,
            token = app_settings.TOKEN,
            channel = app_settings.CHANNEL,
            icon_emoji = app_settings.ICON_EMOJI,
            username = app_settings.USERNAME,
        )

        backend(slack_data, endpoint_url)

        print('message sent')
