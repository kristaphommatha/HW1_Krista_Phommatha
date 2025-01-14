import sys
sys.path.insert(0, '../../src')

from extract_parameter import extract_parameter
import unittest
import os

class TestExtractParameter(unittest.TestCase):
    def test_valid_inputs(self):
        unit_operations_data = {
            "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
            "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
            "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
            }
        expected = "distillation_column_temperature_160"
        result = extract_parameter(unit_operations_data, "distillation_column", "temperature", 1)
        self.assertEqual(expected, result)

    def test_invalid_unit(self):
        unit_operations_data = {
            "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
            "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
            "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
            }
        expected = 'Invalid Input: Unit "centrifuge" not found.'
        test_no_unit = extract_parameter(unit_operations_data, "centrifuge", "temperature", 1)
        self.assertEqual(expected, test_no_unit)

    def test_invalid_parameter(self):
        unit_operations_data = {
            "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
            "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
            "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
            }
        expected = 'Invalid Input: Parameter "reflux_ratio" not found.'
        test_no_parameter = extract_parameter(unit_operations_data, "distillation_column", "reflux_ratio", 1)
        self.assertEqual(expected, test_no_parameter)

    def test_invalid_index(self):
        unit_operations_data = {
            "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
            "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
            "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
            }
        expected = 'Invalid Input: The given unit and parameter combination only has valid index from 0 to 2.'
        test_no_index = extract_parameter(unit_operations_data, "distillation_column", "temperature", 5)
        self.assertEqual(expected, test_no_index)


if __name__ == '__main__':
    unittest.main()