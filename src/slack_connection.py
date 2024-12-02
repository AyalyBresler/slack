
def join_to_channel(client, channelId = '#connection'):
    try:
        client.conversations_join(channel=channelId)

    except Exception as error:
        raise error

def create_a_channel(client, name):
    try:
        client.conversations_create(name=name, is_private=False)

    except Exception as error:
        raise error

def list_of_connections(client):
    try:
        return client.users_list()

    except Exception as error:
        raise error
