import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import fetch_contagem_cores
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):

    def test_contagem_cores(self):
        velas = [
            {
            "created": "Tue, 27 Jun 2023 23:55:09 GMT",
            "platform": "blaze",
            "vela": 1.16
        },
        {
            "created": "Tue, 27 Jun 2023 23:54:56 GMT",
            "platform": "blaze",
            "vela": 2.4
        },
        {
            "created": "Tue, 27 Jun 2023 23:54:32 GMT",
            "platform": "blaze",
            "vela": 1.43
        },
        {
            "created": "Tue, 27 Jun 2023 23:54:16 GMT",
            "platform": "blaze",
            "vela": 1.14
        },
        {
            "created": "Tue, 27 Jun 2023 23:54:04 GMT",
            "platform": "blaze",
            "vela": 11.1
        },
        {
            "created": "Tue, 27 Jun 2023 23:53:13 GMT",
            "platform": "blaze",
            "vela": 11.87
        },
        {
            "created": "Tue, 27 Jun 2023 23:52:22 GMT",
            "platform": "blaze",
            "vela": 12.5
        }
        ]

        result = fetch_contagem_cores(velas)
        self.assertEqual(result['qtdPreta'], 3)
        self.assertEqual(result['qtdVerde'], 4)
        self.assertEqual(result['percentagePreta'], '43%')
        self.assertEqual(result['percentageVerde'], '57%')

if __name__ == '__main__':
    unittest.main()