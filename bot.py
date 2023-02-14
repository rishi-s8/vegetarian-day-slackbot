import slack
from flask import Flask
from slackeventsapi import SlackEventAdapter
import os

SLACK_TOKEN = os.environ["SLACK_TOKEN"]
SIGNING_SECRET = os.environ["SIGNING_SECRET"]

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)

client = slack.WebClient(token=SLACK_TOKEN)
client.chat_postMessage(channel='#vegetarian-day',text='Hello')

if __name__ == "__main__":
    app.run(debug=True)