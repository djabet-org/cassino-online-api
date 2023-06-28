import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import media_intervalo_tempo
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):

    def test_media_min_velas_5x(self):
        velas = [
            {
            "created": "Tue, 27 Jun 2023 20:55:09 GMT",
            "platform": "blaze",
            "vela": 6
        },
        {
            "created": "Tue, 27 Jun 2023 21:00:09 GMT",
            "platform": "blaze",
            "vela": 6
        },
        {
            "created": "Tue, 27 Jun 2023 21:05:09 GMT",
            "platform": "blaze",
            "vela": 7
        },
        {
            "created": "Tue, 27 Jun 2023 21:10:09 GMT",
            "platform": "blaze",
            "vela": 8
        },
        ]

        result = media_intervalo_tempo(velas)
        print(result)
        self.assertEqual(result, '5.00min')

    def test_media_min_velas_3x(self):
        velas = [
            {
            "created": "Tue, 27 Jun 2023 20:55:09 GMT",
            "platform": "blaze",
            "vela": 4
        },
        {
            "created": "Tue, 27 Jun 2023 21:05:09 GMT",
            "platform": "blaze",
            "vela": 3
        },
        {
            "created": "Tue, 27 Jun 2023 21:15:09 GMT",
            "platform": "blaze",
            "vela": 3
        },
        {
            "created": "Tue, 27 Jun 2023 21:25:09 GMT",
            "platform": "blaze",
            "vela": 4
        },
        ]

        result = media_intervalo_tempo(velas)
        print(result)
        self.assertEqual(result, '10.00min')    

if __name__ == '__main__':
    unittest.main()