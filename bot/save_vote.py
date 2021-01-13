import logging
from configs import config
from util import parser,global_vars
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from bot import (llamadas)
from util import (global_vars)
import json

LOGIN, STORE, VOTINGS, VOTING, SAVE_VOTE  = range(5)

#--Guardado del voto final de la persona

def save_vote(update,context):
#--Id de la votación realizada
    selected_option_id=update.message.text.split('-')[0]    
#--Recuperar el usuario para hacer el voto con el id
    user_by_token=llamadas.get_user(global_vars.token)
    usuario = json.loads(user_by_token.text)
    user_id=usuario['id']
#--Parseo de la respuesta según nuestros estándares
    if selected_option_id is 1:
        a = 1
        b = 0
    else: 
        b = 1
        a = 0
    data_dict={'vote':{'a':a,'b': b},
    'voting' :global_vars.voting_selected,
    'voter':user_id,
    'token': global_vars.token
    }
#--Guardado del voto con llamada a la API
    llamadas.save_vote_data(data_dict)
#--Final de la interacción del bot
    update.message.reply_text('La votación ha sido realizada con éxito.', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END