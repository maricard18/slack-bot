import os
import slack
import schedule
import time
import pprint
from dotenv import load_dotenv
from slack import WebClient
from slack.errors import SlackApiError
from datetime import datetime
from data import check_birthdays
# from data import my_daily_task

# users_list()
check_birthdays()

# schedule the daily task
schedule.every().day.at("10:30").do(check_birthdays)


# while loop to keep the scheduler running
while True:
    schedule.run_pending()