# HW1_Krista_Phommatha

## Contents
### extract_parameter.py
    extract_parameter(unit_operations_data, unit_name, parameter_name, index)

#### Parameters:
**unit_operations_data**: A dictionary containing units with parameter information

```
unit_operations_data = {
    "distillation_column": {"temperature": [150, 160, 170],
                            "pressure": [2, 2.5, 3],
                            "flow_rate": [100, 110, 120]},
    "reactor": {"temperature": [250, 260, 270],
                "pressure": [5, 5.5, 6],
                "residence_time": [10, 12, 14]},
    "heat_exchanger": {"temperature_in": [80, 90, 100],
                        "temperature_out": [50, 60, 70],
                        "flow_rate": [200, 210, 220]}
    }
```

**unit_name**: Desired unit name to look up

**parameter_name**: Desired parameter to look up for specified unit

**index**: Desired index to look up value of parameter

#### Usage
**extract_parameters** searches through a dictionary containing data of units and parameters given a unit name, parameter name, and index. It will output a string of the format `{unit_name}_{parameter_name}_{value}` where value is the data at the specified index.

**Example**:
```
example = extract_parameter(unit_operations_data, "distillation_column", "temperature", 1)
print(example)
```

This will print `distillation_column_temperature_160`.

### calculate_solution_weights.py
    calculate_solution_weights(molecular_weights, solutions_needed)

#### Parameters:
**molecular_weights**: A dictionary containing compounds with their molecular weights
```
molecular_weights = {
    'NaCl': 58.44,
    'H2SO4': 98.079,
    'NaOH': 40.00,
    'KMnO4': 158.034,
    'CH3COOH': 60.052
    }
```

**solutions_needed**: A list of compounds needed for a solution and the necessary concentrations
```
solutions_needed = ['NaCl-0.5M', 'H2SO4-0.25M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M']
```

#### Usage:
**calculate_solution_weights** takes in a list with information about compounds and the concentrations needed for a solution. It will go through this list and search for each compound in a dictionary containing data about molecular weights of compounds to calculate the total weight needed to achieve the specified concentration. A list is generated where each entry is of the format `'{compound}-{concentration}-{weight}'`. If the compound is not found, the entry in the list will be `'unknown'`

**Example:**
```
example = calculate_solution_weights(molecular_weights, solutions_needed)
print(example)
```
This will print `['NaCl-0.5M-29.22g', 'H2SO4-0.25M-24.52g', 'NaOH-1M-40.00g', 'unknown', 'CH3COOH-0.3M-18.02g']`.
