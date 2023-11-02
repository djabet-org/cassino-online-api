import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import catalogar_ciclos
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):
    def test_probabilidade_padrao_xadrez_g2_targetVela7(self):
        velas = [
            { 'vela': 2 },
            { 'vela': 2.7 },
            { 'vela': 3 },
            { 'vela': 1 },
            { 'vela': 2 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 2 },
            { 'vela': 2 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 2 },
            { 'vela': 2 },
        ]

        result = catalogar_ciclos(velas)
        print(result)
        self.assertEqual(result['continuo'], 2)    
        self.assertEqual(result['alternado'], 3)    
    
if __name__ == '__main__':
    unittest.main()