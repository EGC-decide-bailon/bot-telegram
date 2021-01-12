import logging
import json
from bot import llamadas
from util import (global_vars)
from configs import config
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)


LOGIN, STORE, VOTINGS, VOTING, SAVE_VOTE  = range(5)

def login(update, context):
    update.message.reply_text("Indique su nombre de usuario y tu contraseña de la siguiente forma: ",
                              reply_markup=ReplyKeyboardRemove())
    update.message.reply_text("Usuario, Contraseña",
                              reply_markup=ReplyKeyboardRemove())
    return STORE


def store(update, context):
    credentials = {}
    next_state = ConversationHandler.END
    for index, i in enumerate(update.message.text.split(", ")):
        if index == 0:
            credentials["username"] = i
        else:
            credentials["password"] = i

    response = llamadas.get_token(credentials)
    if response.status_code == 200:
        global_vars.token = json.loads(response.text)["token"]
        username = credentials['username']
        reply_keyboard = [['Vote']]

        update.message.reply_text('Bienvenido ' + username + '!', reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True))
        next_state = VOTINGS
    else:
        update.message.reply_text(
            "Usuario o contraseña no valido")
        next_state = STORE


    return next_state
