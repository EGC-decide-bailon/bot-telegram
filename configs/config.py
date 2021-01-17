import os

#=======DECIDE============#
URL_BASE = 'https://decide-voting.herokuapp.com/'
API_DECIDE = URL_BASE + 'gateway/'

BOT_TOKEN = os.environ['BOT_TOKEN']

#=======HEROKU============#
WEBHOOK = True
IP = '0.0.0.0'
PORT = '8443'
BOT_URL = 'https://api.telegram.org/bot' + BOT_TOKEN
HEROKU_APP_NAME = 'bot-slack-decide-bailon'