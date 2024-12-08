from slack_sdk import WebClient
from dotenv import load_dotenv
import os

load_dotenv()


def join_to_channel(client, channelId = '#connection'):
    try:
        client.conversations_join(channel=channelId)
        return True

    except Exception as error:
        raise error

def create_a_channel(client, name):
    try:
        client.conversations_create(name=name, is_private=False)
        return True
    
    except Exception as error:
        raise error

def list_of_connections(client):
    try:
        return client.users_list()

    except Exception as error:
        raise error

def connections_to_slack():
    try:
        client=WebClient(token=os.getenv('SLACK_BOT_TOKEN'))
        list_of_connection_to_slack = []
        list_of_connection_to_slack.append(join_to_channel(client, 'C0821NP8NM7'))
        list_of_connection_to_slack.append(create_a_channel(client, 'celebrations')) 
        list_of_connection_to_slack.append(list_of_connections(client))
        print(list_of_connections(client))
        print('succeeded!')
    except Exception as error:
        raise error
