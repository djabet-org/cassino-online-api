import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import calculate_roll_next_color_probability
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):

    def test_numero_cor_probabilidade(self):
        rolls = [
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            
        ]

        result = calculate_roll_next_color_probability(rolls)
        self.assertEqual(result[1]["red"], 28)

    def test_numero_cor_probabilidade_2(self):
        rolls = [
            { 'roll': 1, 'color': 'red' },
            { 'roll': 2, 'color': 'black' },
            { 'roll': 2, 'color': 'black' },
            { 'roll': 2, 'color': 'black' },
            { 'roll': 2, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 2, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            
        ]

        result = calculate_roll_next_color_probability(rolls)
        self.assertEqual(result[1]["red"], 50)

    def test_numero_cor_probabilidade_white(self):
        rolls = [
            { 'roll': 1, 'color': 'red' },
            { 'roll': 2, 'color': 'black' },
            { 'roll': 2, 'color': 'white' },
            { 'roll': 2, 'color': 'black' },
            { 'roll': 2, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 2, 'color': 'white' },
            { 'roll': 1, 'color': 'red' },
            
        ]

        result = calculate_roll_next_color_probability(rolls)
        self.assertEqual(result[1]["white"], 100)    
    
if __name__ == '__main__':
    unittest.main()