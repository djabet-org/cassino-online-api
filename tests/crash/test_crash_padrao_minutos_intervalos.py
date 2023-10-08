import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import probabilidade_padrao_minutos_intervalos
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):

    d = '2023-11-24 09:30:00.000123'
    dt = datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f')
    velas = [
        {
            "created": (dt+timedelta(minutes=3)).timestamp(),
            "platform": "blaze",
            "vela": 2.4
        },
        {
            "created": (dt+timedelta(minutes=4)).timestamp(),
            "platform": "blaze",
            "vela": 1.43
        },
        {
            "created": (dt+timedelta(minutes=4)).timestamp(),
            "platform": "blaze",
            "vela": 1.43
        },
        {
            "created": (dt+timedelta(minutes=4)).timestamp(),
            "platform": "blaze",
            "vela": 5
        },
        {
            "created": (dt+timedelta(minutes=5)).timestamp(),
            "platform": "blaze",
            "vela": 1.14
        },
        {
            "created":(dt+timedelta(minutes=6)).timestamp(),
            "platform": "blaze",
            "vela": 1
        },
        {
            "created": (dt+timedelta(minutes=7)).timestamp(),
            "platform": "blaze",
            "vela": 1.87
        },
        {
            "created": (dt+timedelta(minutes=8)).timestamp(),
            "platform": "blaze",
            "vela": 1.5
        },
        {
            "created": (dt+timedelta(minutes=8)).timestamp(),
            "platform": "blaze",
            "vela": 1.5
        },
        {
            "created": (dt+timedelta(minutes=9)).timestamp(),
            "platform": "blaze",
            "vela": 1.5
        },
        {
            "created": (dt+timedelta(minutes=10)).timestamp(),
            "platform": "blaze",
            "vela": 1.5
        },
        {
            "created": (dt+timedelta(minutes=11)).timestamp(),
            "platform": "blaze",
            "vela": 1.5
        },
        {
            "created": (dt+timedelta(minutes=12)).timestamp(),
            "platform": "blaze",
            "vela": 1.5
        },
        {
            "created": (dt+timedelta(minutes=13)).timestamp(),
            "platform": "blaze",
            "vela": 1.5
        },
        {
            "created": (dt+timedelta(minutes=14)).timestamp(),
            "platform": "blaze",
            "vela": 2
        },
        {
            "created": (dt+timedelta(minutes=15)).timestamp(),
            "platform": "blaze",
            "vela": 1.5
        },
        {
            "created": (dt+timedelta(minutes=16)).timestamp(),
            "platform": "blaze",
            "vela": 1.5
        },
        ]

    def test_probabilidade_padrao_minutos_intervalos(self):
        result = probabilidade_padrao_minutos_intervalos(self.velas)
        self.assertEqual(result[3], '40%')
        self.assertEqual(result[4], '33%')

if __name__ == '__main__':
    unittest.main()