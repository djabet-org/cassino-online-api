import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import probabilidade_aposXx
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):

    targetX = 10

    def test_probabilidade_apos10x_apos2velas(self):
        velas = [
            { 'vela': self.targetX },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 3 },
            { 'vela': 1 },
            { 'vela': 1 },
        ]

        result = probabilidade_aposXx(velas, self.targetX, galho=0)
        self.assertEqual(result['assertividade'], '100%')

    # def test_probabilidade_aposXx_g1(self):
    #     velas = [
    #         { 'vela': self.targetX },
    #         { 'vela': 1 },
    #         { 'vela': 2 },
    #         { 'vela': 1 },
    #         { 'vela': self.targetX },
    #         { 'vela': 3 },
    #         { 'vela': 2 },
    #         { 'vela': 1 },
    #         { 'vela': 1 },
    #         { 'vela': 1 },
    #         { 'vela': self.targetX },
    #         { 'vela': 4 },
    #         { 'vela': 1 },
    #         { 'vela': 1 }
    #     ]

    #     result = probabilidade_aposXx(velas, self.targetX, 4, 1)
    #     self.assertEqual(result['assertividade'], '100%') 

    # def test_probabilidade_aposXx_g2(self):
    #     velas = [
    #         { 'vela': self.targetX },
    #         { 'vela': 1.99 },
    #         { 'vela': 1 },
    #         { 'vela': 2 },
    #         { 'vela': self.targetX },
    #         { 'vela': 3 },
    #         { 'vela': 2 },
    #         { 'vela': 1 },
    #         { 'vela': 1 },
    #         { 'vela': 1 },
    #         { 'vela': self.targetX },
    #         { 'vela': 4 },
    #         { 'vela': 1 },
    #         { 'vela': 1 }
    #     ]

    #     result = probabilidade_aposXx(velas, self.targetX, 4, 2)
    #     self.assertEqual(result['assertividade'], '100%')

    # def test_probabilidade_aposXx_edge_case(self):
    #     velas = [
    #         { 'vela': self.targetX },
    #         { 'vela': 1.99 },
    #         { 'vela': 1 },
    #         { 'vela': 2 },
    #         { 'vela': self.targetX },
    #         { 'vela': 3 },
    #         { 'vela': 2 },
    #         { 'vela': 1 },
    #         { 'vela': 1 },
    #         { 'vela': 1 },
    #         { 'vela': self.targetX },
    #         { 'vela': 4 }           
    #     ]

    #     result = probabilidade_aposXx(velas, self.targetX, 4, 2)
    #     self.assertEqual(result['assertividade'], '100%')

    # def test_probabilidade_aposXx_edge_case_2(self):
        velas = [
            { 'vela': self.targetX },
            { 'vela': self.targetX },           
            { 'vela': self.targetX },                     
            { 'vela': self.targetX },                     
        ]

        result = probabilidade_aposXx(velas, self.targetX, 4, 2)
        self.assertEqual(result['assertividade'], '100%')            
    
if __name__ == '__main__':
    unittest.main()