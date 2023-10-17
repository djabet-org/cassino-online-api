import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import probabilidade_padrao_surf
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):

    def test_padrao_surf_duplo_g2_targetVela8(self):
        velas = [
            { 'vela': 2.4 },
            { 'vela': 2.7 },
            { 'vela': 2.7 },
            { 'vela': 2.7 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 6 },
        ]

        result = probabilidade_padrao_surf(velas, 2, 8, 0)
        self.assertEqual(result[2]['probabilidade'], 0)
    
    
if __name__ == '__main__':
    unittest.main()