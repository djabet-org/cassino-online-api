import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.double_manager import calculate_roll_next_color_probability
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):

    galho = 2

    def test_numero_cor_probabilidade(self):
        rolls = [
            { 'roll': 1, 'color': 'red' },
            { 'roll': 2, 'color': 'red' },
            { 'roll': 3, 'color': 'red' },
            { 'roll': 4, 'color': 'black' },
            { 'roll': 5, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 2, 'color': 'black' },
            { 'roll': 3, 'color': 'black' },
            { 'roll': 10, 'color': 'black' },
            { 'roll': 5, 'color': 'white' },
            
        ]

        result = calculate_roll_next_color_probability(rolls, self.galho)
        self.assertEqual(result[1]["red"], 50 )
        self.assertEqual(result[1]["black"], 100)
        self.assertEqual(result[10]["white"], 100)

if __name__ == '__main__':
    unittest.main()