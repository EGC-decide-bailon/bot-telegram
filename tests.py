import unittest
import requests
import json
from bot import llamadas

URL_BASE = 'https://decide-voting.herokuapp.com/'
URL_GW = URL_BASE + 'gateway/'

class TestMethods(unittest.TestCase):

    def test_login_test(self):
        credentials = {"username": "user", "password":"rinoceronte2"}
        r = requests.post(URL_GW + 'authentication/login' + credentials)
        self.assertEqual(r.status_code,200)

    def test_get_votings(self):
        r = requests.get(URL_GW + 'voting/?id=' + id_votacion)
        self.assertEqual(r.status_code,200)

    def test_get_voting(self):
        id_votacion = 1
        r = requests.get(URL_GW + 'voting/?id=' + id_votacion)
        self.assertEqual(r.status_code,200)

    def test_get_user(self):
        credentials = {"username": "user", "password":"rinoceronte2"}
        token = llamadas.get_token(credentials)
        data = {'token': token}
        r = requests.post(URL_GW + 'authentication/getuser/', data)
        self.assertEqual(r.status_code,200)

    def test_save_vote(self):
        credentials = {"username": "user", "password":"rinoceronte2"}
        token = llamadas.get_token(credentials)
        data = {'token': token}
        user = requests.post(URL_GW + 'authentication/getuser/', data)
        id = user['id']
        data_dict = {
            "vote": { "a": 0,"b": 1},
            "voting": 3,
            "voter": id,
            "token": token}
        headers = {"Authorization":"Token " + token,
            "Content-Type": "application/json"}
        r = requests.post(config.URL_BASE + "store/", json=data_dict, headers = headers)
        self.assertEqual(r.status_code, 200)

    #Test de errores

if __name__ == '__main__':
    unittest.main()