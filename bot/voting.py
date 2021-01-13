import logging
from configs import config
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from util import (global_vars, parser)

LOGIN, STORE, VOTINGS, VOTING, SAVE_VOTE  = range(5)

#--Mostrar la votación elegida junto a su descripción y opciones para votar
def voting(update, context):
    global_vars.voting_selected = update.message.text.split("-")[0]
    voting = parser.parseVoting()
#--Opciones de la votación
    reply_keyboard = parser.createKeyOption(voting['question']['options'])
#--descripción de la votación
    desc = voting['question']['desc']
    update.message.reply_text("Esta votación tiene como descripción: " + desc, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
    return SAVE_VOTE
