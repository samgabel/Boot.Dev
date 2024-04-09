# Sorts list in place -> similar to insertion sort, but slightly less preferred.
# The time complexity is O(n^2)

# Will swap the current element at index "i" with the lowest value element in the entire list. We repeat this for every index index in the list
# Kind of like Bubble-sort, but we only swap 1 element per iteration, so it is slightly more efficient



def selection_sort(nums):
    # For our entire list of integers...
    for i in range(len(nums)):
        # We set a variable `smallest_idx` to i for every iteration to use in the inner loop
        smallest_idx = i
        # For every element after the current outer loop index...
        for j in range(i + 1, len(nums)):
            # We replace the current smallest_idx with a new smallest_idx...
            # this way we will find the smallest possible element for the given index in the outer loop
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        # After we find the smallest element's index we swap it's element with the current element
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums


# ---------------------------------------------------------------


test = [5, 2, 3, 8, 1, 0]
print(selection_sort(test))
