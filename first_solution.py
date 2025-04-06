def first_solution():
    print("Grupo BigBrain 🧠")
    list = [1, 1, 2, 3, 1]
    reference_values = {}
    max_value_key = None
    max_value = 0

    for element in list:
        if element in reference_values:
            reference_values[element] += 1
        else:
            reference_values[element] = 1

        if reference_values[element] > max_value:
            max_value = reference_values[element]
            max_value_key = element
        
        if max_value > len(list) / 2:
            print("The most frequent value is: ", max_value_key, "with a count of: ", max_value)
            break

first_solution()
