from channels.routing import route

from . import consumers

slack_routing = [
    route('slack-notifications', consumers.handle_notification),
]
