import unittest
import requests
import json
from bot import llamadas

URL_BASE = 'https://decide-voting.herokuapp.com/'
URL_GW = URL_BASE + 'gateway/'

class TestMethods(unittest.TestCase):

    def test_login(self):
        credentials = {"username": "user", "password": "rinoceronte2"}
        r = requests.post(URL_GW + 'authentication/login/', credentials)
        self.assertEqual(r.status_code,200)

    def test_get_votings(self):
        r = requests.get(URL_GW + 'voting/?id=')
        self.assertEqual(r.status_code,200)

    def test_get_voting(self):
        id_votacion = 1
        r = requests.get(URL_GW + 'voting/?id=' + str(id_votacion))
        self.assertEqual(r.status_code,200)

    def test_get_user(self):
        credentials = {"username": "user", "password":"rinoceronte2"}
        token_ser = requests.post(URL_GW + 'authentication/login/', credentials)
        token_des = token_ser.json()
        token = token_des['token']
        data = {'token': token}
        r = requests.post(URL_GW + 'authentication/getuser/', data)
        self.assertEqual(r.status_code,200)

    def test_save_vote(self):
        credentials = {"username": "user", "password": "rinoceronte2"}
        token_ser = requests.post(URL_GW + 'authentication/login/', credentials)
        token_des = token_ser.json()
        token = token_des["token"]
        data = {'token': token}
        
        data_dict = {
            "vote": { "a": 0,"b": 1},
            "voting": 3,
            "voter": 2,
            "token": token}
        headers = {"Authorization":"Token " + token,
            "Content-Type": "application/json"}
        r = requests.post(URL_BASE + "store/", json=data_dict, headers = headers)
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()