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

    def test_numero_cor_probabilidade(self):
        rolls = [
            { 'roll': 1, 'color': 'red' },
            { 'roll': 0, 'color': 'red' },
            { 'roll': 3, 'color': 'red' },
            { 'roll': 4, 'color': 'black' },
            { 'roll': 5, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 0, 'color': 'black' },
            { 'roll': 3, 'color': 'black' },
            { 'roll': 10, 'color': 'black' },
            { 'roll': 5, 'color': 'white' },
            { 'roll': 0, 'color': 'white' },
            { 'roll': 5, 'color': 'white' },
        ]

        result = calculate_roll_next_color_probability(rolls, 2)
        self.assertEqual(result[0]["red"]['hit'], 1)
        self.assertEqual(result[0]["red"]['tried'], 3)
        self.assertEqual(result[0]["red"]['probabilidade'], 33)
        self.assertEqual(result[0]["black"]['hit'], 2)
        self.assertEqual(result[0]["black"]['tried'], 3)
        self.assertEqual(result[0]["black"]['probabilidade'], 66)
        self.assertEqual(result[0]["white"]['hit'], 2)
        self.assertEqual(result[0]["white"]['tried'], 3)
        self.assertEqual(result[0]["white"]['probabilidade'], 66)

if __name__ == '__main__':
    unittest.main()