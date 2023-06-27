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

    def test_probabilidade_apos10x_a(self):
        velas = [
            { 'vela': 10 },
            { 'vela': 2 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 10 },
            { 'vela': 1 },
            { 'vela': 2 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 10 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 }
        ]

        result = probabilidade_aposXx(velas, 10, 20, 2)
        self.assertEqual(result['assertividade'], '67%')

    def test_probabilidade_apos10x_b(self):
        velas = [
            { 'vela': 10 },
            { 'vela': 2 },
            { 'vela': 2 },
            { 'vela': 10 },
            { 'vela': 2 },
            { 'vela': 10 },
            { 'vela': 1 },
        ]

        result = probabilidade_aposXx(velas, 10, 20, 2)

        self.assertEqual(result['assertividade'], '67%')  

    def test_probabilidade_apos10x_c(self):
        velas = [
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 10 },
            { 'vela': 1 },
            { 'vela': 10 },
        ]

        result = probabilidade_aposXx(velas, 10, 20, 2)

        self.assertEqual(result['assertividade'], '100%')

    def test_probabilidade_apos10x_d(self):
        velas = [
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 10 },
            { 'vela': 1 },
            { 'vela': 1 },
        ]

        result = probabilidade_aposXx(velas, 10, 20, 2)

        self.assertEqual(result['assertividade'], '0%')                 

if __name__ == '__main__':
    unittest.main()