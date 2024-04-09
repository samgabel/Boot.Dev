# TODO: revisit
# need to go over on Boot.Dev, try to solve on the website with no help

# Doesn't mutate list state, returns new list

# The algorithm consists of two separate functions, `merge_sort` and `merge`.
    ## `merge_sort()` divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
    ## `merge()` is used for merging two sorted lists back into a single sorted list. At the lowest level of recursion, the two "sorted" lists will...
    ## each have a length of 1. Those single element lists will be merged into a sorted list of length two, and we can build from there.



def merge_sort(nums: list[int]) -> list[int]:
    # If the length of A is less than 2, it's already sorted so return it
    if len(nums) < 2:
        return nums
    # Split the input array into two halves down the middle
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    # Call merge_sort() twice, once on each half
    sort_left = merge_sort(left)
    sort_right = merge_sort(right)
    # Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls
    return merge(sort_left, sort_right)


def merge(first: list[int], second: list[int]) -> list[int]:
    # Create an new final list of integers
    final = []
    # Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
    i, j = 0, 0
    # Use a loop to iterate over A and B at the same time. If an element in A is less than or equal to its respective element in B,
    # add it to the final list and increment i. Otherwise, add the item in B to the final list and increment j.
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    # After comparing all the items, there may be some items left over in either A or B (if one of the lists is longer than the other)...
    # add those extra items to the final list.
    if i < len(first):
        final.extend(first[i:])
    if j < len(second):
        final.extend(second[j:])
    # Return the final list.
    return final


#------------------------------------------------------------------


test_list = [1, 9, 7, 5, 8, 8, 16, 17, 1, 0, 4, 9, 4, 6, 1, 3]
# test_list = [1, 5, 3, 9]
print(merge_sort(test_list))
