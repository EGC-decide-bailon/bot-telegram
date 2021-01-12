import logging
from configs import config
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from util import (global_vars, parser)

LOGIN, STORE, VOTINGS, VOTING, SAVE_VOTE  = range(5)


def voting(update, context):
    global_vars.voting_selected = update.message.text.split("-")[0]
    voting = parser.parseVoting()
    reply_keyboard = parser.createKeyOption(voting['question']['options'])
    desc = voting['question']['desc']
    update.message.reply_text("Esta votación tiene como descripción: " + desc, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
    return SAVE_VOTE
