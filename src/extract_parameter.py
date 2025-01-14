## Function Definition
def extract_parameter(unit_operations_data, unit_name, parameter_name, index):
    try:  # Test if unit_name exists within the dict
        test = unit_operations_data[unit_name]
    except KeyError:  # Prints error info if unit_name is not found
        error_msg = f'Invalid Input: Unit "{unit_name}" not found.'
        return error_msg
    try:  # Test if parameter_name exists under the unit_name in the dict
        test = unit_operations_data[unit_name][parameter_name]
    except KeyError:  # Prints error info if unit_name is not found
        error_msg = f'Invalid Input: Parameter "{parameter_name}" not found.'
        return error_msg
    try:  # Grab value at the given index for unit and parameter combo
        valid_index_range = len(unit_operations_data[unit_name][parameter_name])  # grabbing a valid index range for error handling
        value = str(unit_operations_data[unit_name][parameter_name][index])  #  grabbing value and turning it to string type
        return unit_name + '_' + parameter_name + '_' + value  #  returns string
    except IndexError:  # Prints error info if index is outside of range
        error_msg = f'Invalid Input: The given unit and parameter combination only has valid index from 0 to {valid_index_range-1}.'
        return error_msg
    except Exception as e:
        print(f'Error: {e}')
        return -1