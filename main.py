import logging
import os
from configs import config
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from bot import (login, start, voting, votings,error,cancel,llamadas,save_vote,cancel)
from util import global_vars

LOGIN, STORE, VOTINGS, VOTING, SAVE_VOTE  = range(5)

#--Estado inicial del bot, comando /start para empezar a usarlo------------------

def main():
    updater = Updater(config.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start.start)],

#--Posibles estados y funciones del bot------------------------------------------

        states={

            LOGIN: [MessageHandler(Filters.regex('^(Login)$'), login.login)],

            STORE: [MessageHandler(Filters.text, login.store)],

            VOTINGS: [MessageHandler(Filters.regex('^(Vote)$'), votings.votings)],

            VOTING: [MessageHandler(Filters.text, voting.voting)],

            SAVE_VOTE: [MessageHandler(Filters.text,save_vote.save_vote)]
        },

        fallbacks=[CommandHandler('cancel', cancel.cancel)]
    )
    dp.add_handler(conv_handler)
    dp.add_error_handler(error.error)

if __name__ == '__main__':
    main()
