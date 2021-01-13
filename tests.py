import requests
import unittest
import json

URL_BASE = 'https://decide-voting.herokuapp.com/'
URL_GW = URL_BASE + 'gateway/'

class TestMethods(unittest.TestCase):

    def login_test(self):
        credentials = {"username": "user", "password":"rinoceronte2"}
        r = requests.post(URL_GW + 'authentication/login' + credentials)
        self.assertEqual(r.status_code,200)