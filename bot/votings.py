import logging
from configs import config
from util import parser
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove,message)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from bot import (llamadas)
from util import (global_vars)
import json


LOGIN, STORE, VOTINGS, VOTING, SAVE_VOTE  = range(5)

def votings(update, context):
    response = llamadas.get_user(global_vars.token)
    usuario = json.loads(response.text)

 #Llamada y carga de votaciones 
    response2 = llamadas.get_votings(usuario["id"])
    votos = json.loads(response2.text)

 # Parseo de votos
    votaciones = parser.parseVotings(votos)
    global_vars.user_votings = votaciones
# Parseo de las respuestas de los votos para mostrarlas como botones
    botones = parser.createKeybVoting(votaciones)
    update.message.reply_text('Cargando votaciones!', reply_markup=ReplyKeyboardMarkup(
        botones, one_time_keyboard=True))

    return VOTING
