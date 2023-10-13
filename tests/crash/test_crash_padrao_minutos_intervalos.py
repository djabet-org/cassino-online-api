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

    def test_probabilidade_padrao_minutos_intervalos(self):
        velas = [ 
        {
            "created": (self.dt+timedelta(minutes=3)).timestamp(),
            "platform": "blaze",
            "vela": 2.4
        },
        {
            "created": (self.dt+timedelta(minutes=4)).timestamp(),
            "platform": "blaze",
            "vela": 1.43
        },
        ]

        result = probabilidade_padrao_minutos_intervalos(velas, 0)
        self.assertEqual(result[3], '100%')
    def test_probabilidade_padrao_minutos_intervalos_nao_achou(self):
        velas = [ 
        {
            "created": (self.dt+timedelta(minutes=3)).timestamp(),
            "platform": "blaze",
            "vela": 1.1
        },
        {
            "created": (self.dt+timedelta(minutes=4)).timestamp(),
            "platform": "blaze",
            "vela": 1.2
        },
        ]

        result = probabilidade_padrao_minutos_intervalos(velas, 0)
        self.assertEqual(result[3], '0%')

    def test_probabilidade_padrao_minutos_intervalos_g2(self):
        velas = [ 
        {
            "created": (self.dt+timedelta(minutes=3)).timestamp(),
            "platform": "blaze",
            "vela": 1.1
        },
        {
            "created": (self.dt+timedelta(minutes=4)).timestamp(),
            "platform": "blaze",
            "vela": 1.2
        },
        {
            "created": (self.dt+timedelta(minutes=4)).timestamp(),
            "platform": "blaze",
            "vela": 3
        },
        ]

        result = probabilidade_padrao_minutos_intervalos(velas, 2)
        self.assertEqual(result[3], '100%')    
    def test_probabilidade_padrao_minutos_intervalos_g2_nao_achou(self):
        velas = [ 
        {
            "created": (self.dt+timedelta(minutes=3)).timestamp(),
            "platform": "blaze",
            "vela": 1.1
        },
        {
            "created": (self.dt+timedelta(minutes=4)).timestamp(),
            "platform": "blaze",
            "vela": 1.2
        },
        {
            "created": (self.dt+timedelta(minutes=4)).timestamp(),
            "platform": "blaze",
            "vela": 1.3
        },
        ]

        result = probabilidade_padrao_minutos_intervalos(velas, 2)
        self.assertEqual(result[3], '0%')    
    
    def test_probabilidade_padrao_minutos_intervalos_targetVela(self):
        velas = [ 
        {
            "created": (self.dt+timedelta(minutes=3)).timestamp(),
            "platform": "blaze",
            "vela": 5
        },
        {
            "created": (self.dt+timedelta(minutes=4)).timestamp(),
            "platform": "blaze",
            "vela": 1.1
        },
        {
            "created": (self.dt+timedelta(minutes=4)).timestamp(),
            "platform": "blaze",
            "vela": 1.2
        },
        ]

        result = probabilidade_padrao_minutos_intervalos(velas, 2, 5)
        self.assertEqual(result[3], '100%')    
    def test_probabilidade_padrao_minutos_intervalos_targetVela_nao_achou(self):
        velas = [ 
        {
            "created": (self.dt+timedelta(minutes=3)).timestamp(),
            "platform": "blaze",
            "vela": 4
        },
        {
            "created": (self.dt+timedelta(minutes=4)).timestamp(),
            "platform": "blaze",
            "vela": 1.1
        },
        {
            "created": (self.dt+timedelta(minutes=4)).timestamp(),
            "platform": "blaze",
            "vela": 1.2
        },
        ]

        result = probabilidade_padrao_minutos_intervalos(velas, 2, 5)
        self.assertEqual(result[3], '0%')    

if __name__ == '__main__':
    unittest.main()