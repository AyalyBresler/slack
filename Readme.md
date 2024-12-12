# SLACK

### Create an automatic connection list to Slack via the WEB API.

Create an App in the Slack, via use WebClient from slack_sdk module with the bot token of the app.
for example:
    `WebClient(token=os.getenv('SLACK_BOT_TOKEN'))`
then create list that:
- create a conversations to join to slack according  to the channel id of the channel.
- create a conversations to create a new channel with the channel name in the slack,
- return the list of the users- conversations via the WEB API in the slack!
