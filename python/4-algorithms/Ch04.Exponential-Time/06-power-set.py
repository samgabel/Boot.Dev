# Complete the power_set function using the following algorithm:
# 1. Check if the input list is empty. If it is, return a list containing an empty list. (The power set of an empty set is a set containing just the empty set)
# 2. Otherwise, create an empty list to hold all the final subsets of the input list.
# 3. Recursively call power_set. Pass in all of the elements in the input set except the first one.
# 4. Iterate over the list of subsets returned from the recursive call. For each subset, append two new subsets to the final list of subsets:
#   a. first_item_from_input_set + subset
#   b. subset


def power_set(input_set: list[int]) -> list[list[int]]:
    # 1
    if input_set == []:
        return [input_set]
    # 2
    final_set = []
    # 3
    sets = power_set(input_set[1:])
    # 4
    for s in sets:
        # a
        final_set.append([input_set[0]] + s)
        # b
        final_set.append(s)

    return final_set


# if __name__ == "__main__":
input_list = [1, 2, 3]
print(power_set(input_list))
# [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]
