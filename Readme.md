# SLACK

### Create an automatic connection list to Slack via the WEB API.

Create an App in the Slack, via use WebClient from slack_sdk module with the bot token of the app.
for example:
    `client = WebClient(token=os.getenv('SLACK_BOT_TOKEN'))`

To run this program in the docker:

```cmd
docker build -t <name> .
docker run -p 5000:5000 -it <name>
``` 

then create list that:
- create a conversations to join to slack according  to the channel id of the channel.
run:
    `client.conversations_join(channel=channelId)`

- create a conversations to create a new channel with the channel name in the slack,
run:
    `client.conversations_create(name=name)`

- return the list of the users- conversations via the WEB API in the slack!
run:
    `client.users_list()`
