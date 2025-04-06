# Boyer-Moore Solution
def optimal_solution():
    list = [1, 3, 3, 3, 2, 3, 3]
    candidate = None
    count = 0

    for element in list:
        if count == 0:
            candidate = element
            count = 1
        elif element == candidate:
            count += 1
        else:
            count -= 1

    candidate_count = 0
    for element in list:
        if element == candidate:
            candidate_count += 1

    if candidate_count > len(list) // 2:
        print("The majority element is:", candidate, "with a count of:", candidate_count)
    else:
        print("There is no majority element")

optimal_solution()