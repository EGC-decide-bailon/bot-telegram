import logging
from configs import config
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)


LOGIN, STORE, VOTINGS, VOTING, SAVE_VOTE  = range(5)

def start(update, context):
    reply_keyboard = [['Login']]
    update.message.reply_text(
        'Hola! Soy el Bot de la Cabina del sistema Decide. Vota! Te ayudo.',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return LOGIN
