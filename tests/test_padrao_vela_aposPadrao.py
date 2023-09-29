import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import probabilidade_aposPadrao
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):

    def test_probabilidade_aposPadrao_duplo(self):
        velas = [
            { 'vela': 2.4 },
            { 'vela': 2.7 },
            { 'vela': 1 },
            { 'vela': 2 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 2 },
            { 'vela': 3 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 }
        ]

        result = probabilidade_aposPadrao(velas, 2, 2, 3, 2)
        self.assertEqual(result, '50%')

    def test_probabilidade_aposPadrao_duplo_2(self):
        velas = [
            { 'vela': 2.4 },
            { 'vela': 2.7 },
            { 'vela': 1 },
            { 'vela': 2 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 2 },
            { 'vela': 3 },
            { 'vela': 6 },
        ]

        result = probabilidade_aposPadrao(velas, 2, 2, 3, 2)
        self.assertEqual(result, '100%')    

    def test_probabilidade_aposPadrao_duplo_3(self):
        velas = [
            { 'vela': 2.4 },
            { 'vela': 2.7 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 2 },
            { 'vela': 3 },
            { 'vela': 1 },
        ]

        result = probabilidade_aposPadrao(velas, 2, 2, 3, 2)
        self.assertEqual(result, '0%') 

    def test_probabilidade_aposPadrao_duplo_4(self):
        velas = [
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
        ]

        result = probabilidade_aposPadrao(velas, 2, 2, 3, 2)
        self.assertEqual(result, '0%')            
    
if __name__ == '__main__':
    unittest.main()