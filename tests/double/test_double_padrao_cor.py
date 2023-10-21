import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.double_manager import probabilidade_padrao_cor
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):

    def test_padrao_cores(self):
        rolls = [
            { 'roll': 1, 'color': 'red' },
            { 'roll': 2, 'color': 'red' },
            { 'roll': 3, 'color': 'black' },
            { 'roll': 4, 'color': 'red' },
            { 'roll': 5, 'color': 'black' },
            { 'roll': 6, 'color': 'red' },
            { 'roll': 7, 'color': 'red' },
            { 'roll': 8, 'color': 'black' },
            { 'roll': 9, 'color': 'red' },
            { 'roll': 10, 'color': 'black' },
            { 'roll': 11, 'color': 'red' },
            { 'roll': 12, 'color': 'red' },
            
        ]

        self.assertEqual(probabilidade_padrao_cor(rolls, 'r,b,r', 'red', 2)['probabilidade'], 100)
        self.assertEqual(probabilidade_padrao_cor(rolls, 'r,r', 'red', 2)['probabilidade'], 100)
        self.assertEqual(probabilidade_padrao_cor(rolls, 'r,r,r', 'red', 2)['probabilidade'], 0)

if __name__ == '__main__':
    unittest.main()