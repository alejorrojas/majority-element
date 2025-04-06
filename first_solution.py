def first_solution():
    list = [1, 1, 2, 3, 1]
    reference_values = {}
    max_value_key = None
    max_value = 0

    for element in list:
        if element in reference_values:
            reference_values[element] += 1
        else:
            reference_values[element] = 1

        # Update the most frequent element on the same loop, avoiding the need to iterate through the dictionary again
        if reference_values[element] > max_value:
            max_value = reference_values[element]
            max_value_key = element
        
        #Early return if the most frequent value is greater than half of the list
        if max_value > len(list) / 2:
            print("The most frequent value is: ", max_value_key, "with a count of: ", max_value)
            break

first_solution()
