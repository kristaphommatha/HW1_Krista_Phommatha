def calculate_solution_weights(molecular_weights, solutions_needed):
    output_list = []  # initialize list to output
    for entry in solutions_needed:  # use for loop to go through solutions_needed list
        solution = entry.split('-')  # separates the compound name and concentration in string
        compound = solution[0]  # first part is compound name
        concentration_str= solution[1]  # second part is concentration
        concentration = float(concentration_str[:-1])  # turns the second part into a float to calculate weight later. :-1 to remove M unit label
        try:  # try to find compound in molecular_weights dict
            molecular_weight = molecular_weights[compound]
            weight = molecular_weight * concentration
            output_list.append(compound + '-' + concentration_str + '-' + f'{weight:.{2}f}' + 'g')  # add entry to empty list with weight having 2 decimal points
        except KeyError:  # if the compound is not found in the dict
            output_list.append('unknown')  # add 'unknown' to the list
    return output_list
