import logging
from configs import config
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

def cancel(update, context):

    update.message.reply_text('Adios! escribe /start para volver a iniciar', reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END
