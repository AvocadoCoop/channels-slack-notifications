from channels import Channel


def send(text, data=None, channel_name='slack-notifications'):
    if data is None:
        data = {}

    data['text'] = text
    Channel(channel_name).send(data)
