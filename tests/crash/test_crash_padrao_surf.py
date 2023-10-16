import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import probabilidade_padrao_surf
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):

    def test_padrao_surf_duplo(self):
        velas = [
            { 'vela': 2.4 },
            { 'vela': 2.7 },
            { 'vela': 3 },
            { 'vela': 2 },
            { 'vela': 6 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
        ]

        result = probabilidade_padrao_surf(velas, galho=0)
        self.assertEqual(result[2]['probabilidade'], 50)
    
    def test_padrao_surf_triplo(self):
        velas = [
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 2.3 },
            { 'vela': 2.4 },
            { 'vela': 2.5 },
            { 'vela': 2.6 },
            { 'vela': 2.7 },
            { 'vela': 2.8 },
            { 'vela': 6 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
        ]

        result = probabilidade_padrao_surf(velas, galho=0)
        self.assertEqual(result[3]['probabilidade'], 50)

    def test_padrao_surf_g2(self):
        velas = [
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 2.3 },
            { 'vela': 2.4 },
            { 'vela': 2.5 },
            { 'vela': 2.6 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 6 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
        ]

        result = probabilidade_padrao_surf(velas, galho=2 )
        self.assertEqual(result[2]['probabilidade'], 100)

    def test_padrao_surf_g2_targetVela(self):
        velas = [
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 2.3 },
            { 'vela': 2.4 },
            { 'vela': 2.5 },
            { 'vela': 2.6 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 23},
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
        ]

        result = probabilidade_padrao_surf(velas, galho=2, targetVela=3 )
        self.assertEqual(result[2]['probabilidade'], 100)

    def test_padrao_surf_g2_targetVela_minProbabilidade(self):
        velas = [
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 2.3 },
            { 'vela': 2.4 },
            { 'vela': 2.5 },
            { 'vela': 2.6 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 23},
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
        ]

        result = probabilidade_padrao_surf(velas, galho=2, targetVela=3, minProbabilidade=90 )
        self.assertEqual(result[2]['probabilidade'], 100)    
    
if __name__ == '__main__':
    unittest.main()