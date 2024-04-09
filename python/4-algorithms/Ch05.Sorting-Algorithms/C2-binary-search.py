# This is a way to quickly search through a sorted list of elements
# Since we reduce our search radius by half everytime, we only have a time complexity of `O(log(n))`



def binary_search(data, followers):
    # Set a left (l) to be the first index of the list and a right (r) to be the last index
    l = 0
    r = len(data) - 1
    # Continue to loop only until we have no more values in our range of l to r
    while l <= r:
        # Set mid to be the middle point of l and r of this iteration
        mid = (l + r) // 2
        # If our follower count at mid is *less* than our target count then...
        if data[mid]["followers"] < followers:
            # we want to only concern ourselves with everything to the *right* of mid
            l = mid + 1
        # If our follower count at mid is *greater* than our target count then...
        elif data[mid]["followers"] > followers:
            # we want to only concern ourselves with everything to the *left* of mid
            r = mid - 1
        # Return the "name" value of the mid index if it happens to be our target index
        else:
            return data[mid]["name"]
    # Return None if the value is not found
    return None


# ------------------------------------------------------------------------------------


test = [
    {'name': 'Guy', 'followers': 15},
    {'name': 'Nye', 'followers': 40},
    {'name': 'Bill', 'followers': 50},
]
print(binary_search(test, 40))
