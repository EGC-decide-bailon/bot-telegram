import logging
from configs import config
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
def error(update, context):

    update.message.reply_text('Ha ocurrido un error en el proceso, escriba "/start" para volver a empezar.',
                            reply_markup=ReplyKeyboardRemove())   
    return ConversationHandler.END

