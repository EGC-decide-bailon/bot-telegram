import requests
from configs import config

#--Recuperar token del usuario
def get_token(credentials):

    r = requests.post(config.API_DECIDE + "authentication/login/", credentials)

    return r

#--Recuperar votación
def get_votings(id):
    r = requests.get(config.API_DECIDE + "voting/?id="+str(id))
    return r

#--Recuperar info del usuario
def get_user(token):
    data = {'token': token}
    r = requests.post(config.API_DECIDE + "authentication/getuser/", data)
    return r

#--Guardado del voto
def save_vote_data(data_dict):
    
    headers = {"Authorization": "Token " + data_dict['token'],
                "Content-Type": "application/json"}
    
    r = requests.post(config.URL_BASE + "store/", json=data_dict, headers = headers)

    print(r.status_code)
    return r



