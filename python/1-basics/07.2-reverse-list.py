def reverse_array(items):
    last_index = len(items) - 1
    reverse_list = []
    for i in range(last_index, -1, -1):
        reverse_list.append(items[i]) 
    return reverse_list

# TEST CASES ----------------------
items = [1, 2, 3, 4, 5]
# items = []
# items = ["horse", "sheep", "dog"]
# items = ["a", "a"]

# PRINT TO CONSOLE ----------------
print(reverse_array(items))
