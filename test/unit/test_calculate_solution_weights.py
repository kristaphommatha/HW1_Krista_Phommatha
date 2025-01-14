import sys
sys.path.insert(0, '../../src')

from calculate_solution_weights import calculate_solution_weights
import unittest
import os

class TestCalculateSolutionWeights(unittest.TestCase):
    def test_working_case(self):
        molecular_weights = {
            'NaCl': 58.44,
            'H2SO4': 98.079,
            'NaOH': 40.00,
            'KMnO4': 158.034,
            'CH3COOH': 60.052
            }
        solutions_needed = ['NaCl-0.5M', 'H2SO4-0.25M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M']

        expected_list = ['NaCl-0.5M-29.22g', 'H2SO4-0.25M-24.52g', 'NaOH-1M-40.00g', 'unknown', 'CH3COOH-0.3M-18.02g']
        result = calculate_solution_weights(molecular_weights, solutions_needed)
        self.assertListEqual(expected_list, result)

if __name__ == '__main__':
    unittest.main()
        