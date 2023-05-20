import os
import slack
import schedule
import time
import pprint
from dotenv import load_dotenv
from slack import WebClient
from slack.errors import SlackApiError
from datetime import datetime

# load the .env file to get the token
env_path = ".env"
load_dotenv(env_path)

# get the token from the environment variable
client = slack.WebClient(token = os.environ['SLACK_TOKEN'])

class Data:
    def __init__(self, id, user, day, month):
        self.id = id
        self.user = user
        self.day = day
        self.month = month

people = [
    Data("U058CQ58LMB", "Mario", 20, 5),
	Data("U058Q5FKBRR", "Joao", 20, 5),
	Data("USLACKBOT", "Slackbot", 23, 11),
]    

# function to check if there is a birthday today
def check_birthdays():
	# Get the current date
	today = datetime.now()

	# Get the people with a birthday today
	birthday_people = [person for person in people if person.day == today.day and person.month == today.month]

	# Check the number of people with a birthday today
	num_people = len(birthday_people)

	# Generate the birthday message
	if num_people > 1:
    	# Multiple people have a birthday today
		mention_list = [f"<@{person.id}|{person.user}>" for person in birthday_people]
		names = ' && '.join(mention_list)
		message = f"Happy Birthday to {names}! :tada: :confetti_ball:"
	
	elif num_people == 1:
    	# Only one person has a birthday today
		person = birthday_people[0]
		mention = f"<@{person.id}|{person.user}>"
		message = f"Happy Birthday to {mention} :tada: :confetti_ball:"
			
	client.chat_postMessage(
		channel='#general',
		text=message)
	

# function to get the list of users
# def users_list():
#     list = client.users_list()

#     if list['ok']:
#         users = list['members']

#         for user in users:
#                 id = user['id']
#                 username = user['profile']['display_name']
#                 print(id, username)
#     else:
#         print(f"Error: {list['error']}")  