import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import media_velas
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):

    def test_media_velas(self):
        velas = [
            {
            "created": 1698370802,
            "platform": "blaze",
            "vela": 4
        },
        {
            "created": 1698371042,
            "platform": "blaze",
            "vela": 4.1
        },
         {
            "created": 1698371282,
            "platform": "blaze",
            "vela": 4.2
        },
        {
            "created": 1698371162,
            "platform": "blaze",
            "vela": 8
        }
        ]

        result = media_velas(velas)
        self.assertEqual(result['3x']['qtd'], 3)
        self.assertEqual(result['3x']['media'], 75)
        self.assertEqual(result['3x']['media_tempo'], '4.00min')

if __name__ == '__main__':
    unittest.main()