****************************
Channels Slack Notificaitons
****************************

If you want to asyncronously send low priority messages to a
Slack channel using `Django Channels <https://channels.readthedocs.io/en/latest/>`_
this is the 3rd party library for you.

Partially inspired by django-slack https://github.com/lamby/django-slack. Adding support for channels and simplying the interface.

Requirements
############

#. Django 1.8+
#. channels
#. requests

Quick Start
###########

Add to ``INSTALLED_APPS`` and set your slack token::

    INSTALLED_APPS = (
      # ...
      'channels_slack_notifications',
      # ...
    )

    CHANNELS_SLACK_TOKEN = 'yourtokenhere'

You can generate a tokens here: https://api.slack.com/web#authentication

Add to your ``routing.py``::

    from channels.routing import include
    from channels_slack_notifications.routing import slack_routing

    channels_routing = [
        include(slack_routing),
    ]


Send your first notification::

    from channels_slack_notifications

    message = dict(
        text = 'this is a test',
    )
    Channel('slack-notifications').send(message)

This uses a bunch of defaults which you can override per setting, or just in the message dict.

You can use this management command to test your settings::

    python manage.py test_slack_notification

Settings
########

``CHANNELS_SL
ACK_TOKEN``
~~~~~~~~~~~~~~~~~~~~~~~~

Default: ``None``

Your Slack authentication token.

You can generate a tokens here: https://api.slack.com/web#authentication

``CHANNELS_SLACK_CHANNEL``
~~~~~~~~~~~~~~~~~~~~~~~~~~
Default: ``#general``

Use this setting to set a default channel of the room the message should appear
in.

You can override on a per-message level by specifying ``channel`` in your message dict.

``CHANNELS_SLACK_USERNAME``
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Default: ``bot``

Use this setting to set a default name the message will appear be sent from.

You can override on a per-message level by specifying ``username`` in your message dict.

``CHANNELS_SLACK_ICON_EMOJI``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Default: ``:robot:``

Use this setting to set a default icon emoji.

You can override on a per-message level by specifying ``icon_emoji`` in your message dict.

``CHANNELS_SLACK_BACKEND``
~~~~~~~~~~~~~~~~~~~~~~~~~~
Default: ``'channels_slack_notifications.backends.console'``

A string pointing to the eventual backend class that will actually send the
message to the Slack API.

Use ``'channels_slack_notifications.backends.default'`` in product which uses the requests library.
