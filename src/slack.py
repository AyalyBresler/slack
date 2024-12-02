from slack_sdk import WebClient
from dotenv import load_dotenv
import slack_connection
import os

load_dotenv()
slack_token = os.getenv('SLACK_BOT_TOKEN')

def connections_to_slack():
    client=WebClient(token=slack_token)
    list_of_connection_to_slack = []
    list_of_connection_to_slack.append(slack_connection.join_to_channel(client, 'C0821NP8NM7'))
    list_of_connection_to_slack.append(slack_connection.create_a_channel(client, 'celebrate')) 
    list_of_connection_to_slack.append(slack_connection.list_of_connections(client))
    print('succeeded!')


connections_to_slack()
