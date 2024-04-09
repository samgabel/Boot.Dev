# Sorts list in place

# Time Complexity...
    ## Big O -> O(n^2)          -> "Big O" or Worst-case Scenario
    ## Big Ω -> O(n * log(n))   -> "Big Omega" or Best-case Scenario
    ## Big Θ -> O(n * log(n))   -> "Big Theta" or Average-case Scenario

# `quick_sort()` will call `partition()` and then call itself for the left and right side of the "pivot" (returned by `partition()`)
# `partition()` serves to set a pivot and sets all the elements less than the pivot to the left, leaving elements greater than the pivot to the right



def quick_sort(nums: list[int], low: int, high: int) -> list[int]:
    # we want to run each recursion until there are no more numbers in the list to sort
    if low < high:
        # eveytime we recurse, we call the `partition()` function which will sort the elements in place
        # on the first call we roughly sort the entire list, where each recursion will sort a little more precisely
        pivot_index = partition(nums, low, high)
        # 1st recursion onwards we will run quick sort on the list before and after the pivot index
        quick_sort(nums, low, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, high)
    return nums


def partition(nums: list[int], low: int, high: int) -> int:
    # We set the pivot to be the element in index -> `high` (right-most element)
    pivot = nums[high]
    # Set i and j to be equal
    i = low
    # For every element in our range...
    for j in range(low, high):
        # We will switch the elements at i and j if the element at j happens to be smaller than the pivot
        # If the element at j is not smaller, then we know that for the current element at j and...
        # any future element that is smaller than the pivot we will have to swap spots
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            # This keeps track of the new element being tested / the element bigger than the pivot
            # it also doubles as the index at which the pivot will reside
            i += 1
    # After the loop completes we want to put the pivot in it's rightful index location
    nums[i], nums[high] = nums[high], nums[i]
    # We want to return the pivot index location for future recursive calls
    return i


# We could improve the current design by implementing the "median of median"...
# We could also randomly shuffle the input list to enure the list is not in order which works practically all the time
# This way, our time complexity averages to be more towards O(n * log(n))


# ------------------------------------------------------


test = [3, 7, 1, 2, 7, 5, 4]
print(quick_sort(test, 0, len(test) - 1))
