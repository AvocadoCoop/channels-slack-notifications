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

Add to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
      # ...
      'channels_slack_notifications',
      # ...
    )

Add to your ``routes.py``::

    # TODO


Send your first notification::

    from channels_slack_notifications

    message = dict(
        message = 'this is a test',
    )
    Channel('slack-notifications').send(message)

This uses a bunch of defaults which you can override per setting, or just in the message dict.

Settings
########

``CHANNELS_SLACK_TOKEN``
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

``SLACK_ENDPOINT_URL``
~~~~~~~~~~~~~~~~~~~~~~
Default: ``https://slack.com/api/chat.postMessage``
Use this setting to set a default endpoint URL. This is necessary to use
Slack's "Incoming Webhooks."
You can override on a per-message level by specifying a
``{% block endpoint_url %}{% endblock %}`` in your message template.