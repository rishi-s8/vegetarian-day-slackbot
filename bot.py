import time
import datetime
import pause
import slack
import os

SLACK_TOKEN = os.environ["SLACK_TOKEN"]

client = slack.WebClient(token=SLACK_TOKEN)

weekday = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
possibledays = ["Monday","Tuesday","Thursday"]

veggyday = datetime.datetime.fromisoformat('2023-01-09')

def is_veggie_day(dt:datetime.date):
    day = weekday[dt.weekday()]
    if day in possibledays:
        t_delta = dt - veggyday
        num_days_since_veggyday = t_delta.days
        return (day == "Thursday" and (num_days_since_veggyday-17)%21 == 0) or (day == "Monday" and (num_days_since_veggyday)%21 == 0) or (day == "Tuesday" and (num_days_since_veggyday-8)%21 == 0)
    else:
        return False

while True:
    if datetime.datetime.now().hour >= 10:
        tomorrow_date = datetime.datetime.today() + datetime.timedelta(days=1)
        wakeupTime = datetime.datetime(tomorrow_date.year, tomorrow_date.month, tomorrow_date.day, 10, 0, 0, 0)
    else:
        today_date = datetime.datetime.today()
        wakeupTime = datetime.datetime(today_date.year, today_date.month, today_date.day, 10, 0, 0, 0)
    pause.until(wakeupTime)

    today_date = datetime.datetime.today()
    tomorrow_date = today_date + datetime.timedelta(days=1)

    if is_veggie_day(today_date):
        client.chat_postMessage(channel='#vegetarian-day',text="Today is Vegetarian Day! :broccoli:")
    elif is_veggie_day(tomorrow_date):
        client.chat_postMessage(channel='#vegetarian-day',text="Tomorrow is Vegetarian Day! :avocado:")


