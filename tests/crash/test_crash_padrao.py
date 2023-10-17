import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import probabilidade_padrao
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):

    # def test_probabilidade_padrao_surf_g2_targetVela7(self):
    #     velas = [
    #         { 'vela': 1 },
    #         { 'vela': 2.7 },
    #         { 'vela': 3 },
    #         { 'vela': 2 },
    #         { 'vela': 2 },
    #         { 'vela': 1},
    #         { 'vela': 1 },
    #         { 'vela': 7 },
    #         { 'vela': 1 },
    #         { 'vela': 1 },
    #         { 'vela': 1 },
    #         { 'vela': 1 },
    #         { 'vela': 2 },
    #         { 'vela': 2 },
    #         { 'vela': 2 },
    #         { 'vela': 2 },
    #         { 'vela': 6 },
    #     ]

    #     result = probabilidade_padrao(velas, galho=2, targetVela=6, padrao=[2,2,2,2])
    #     self.assertEqual(result['probabilidade'], 100)

    def test_probabilidade_padrao_xadrez_g2_targetVela7(self):
        velas = [
            { 'vela': 1 },
            { 'vela': 2.7 },
            { 'vela': 1 },
            { 'vela': 2 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 7 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 2 },
            { 'vela': 1 },
            { 'vela': 4 },
            { 'vela': 1 },
            { 'vela': 4},
        ]

        result = probabilidade_padrao(velas, galho=2, targetVela=6, padrao=[2,1,2,1])
        self.assertEqual(result['probabilidade'], 50)    
    
if __name__ == '__main__':
    unittest.main()