def sum_nested_list(lst):
    count = 0
    for item in lst:
        if isinstance(item, int):
            count += item
        else:
            # using recursion on instances of lists so that we can add the count of nested lists
            count += sum_nested_list(item)
    return count


# -----------------------------------------


nested_list = [5, [6, 7], [[8, 9], 10]]
print("The sum of the values in the nested list is:", sum_nested_list(nested_list))
