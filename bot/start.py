import logging
from configs import config
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)


LOGIN, STORE, VOTINGS, VOTING, SAVE_VOTE  = range(5)

#--Respuesta del bot al comando inicial-----------------------------

def start(update, context):
    boton_login = [['Login']]
    update.message.reply_text(
        'Hola! Soy el Bot de la Cabina del sistema Decide. Vota! Te ayudo.',
        reply_markup=ReplyKeyboardMarkup(boton_login, one_time_keyboard=True))

    return LOGIN
