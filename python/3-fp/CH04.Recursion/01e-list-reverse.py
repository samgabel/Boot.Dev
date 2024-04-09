def print_list(lst, i):
    if len(lst) == i:
        return
    # putting the function call before the action will print the list in reverse
    # becuase the function will recurse all the way before hitting the first print statement (of last function)
    print_list(lst, i+1)
    print(lst[i])

#----------------------------------------------------

print_list(["apple", "pear", "orange"], 0)
