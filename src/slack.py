from slack_sdk import WebClient
from dotenv import load_dotenv
import os

load_dotenv()
slack_token = os.getenv('SLACK_BOT_TOKEN')

def connections_to_slack():
    client=WebClient(token=slack_token)
    join_to_channel(client, 'C0821NP8NM7')
    create_a_channel(client, 'celebrate')
    list_of_connections(client)
    print('succeeded!')


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

connections_to_slack()
