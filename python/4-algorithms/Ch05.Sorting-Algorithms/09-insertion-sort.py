def insertion_sort(nums: list[int]) -> list[int]:
    # For each index in the input list:
    for i in range(len(nums)):
        # Set a j variable to the current index
        j = i
        # While j is greater than 0 and the element at index j-1 is greater than the element at index j:
        while j > 0 and nums[j - 1] > nums[j]:
            # Swap the elements at indices j and j-1
            # in this case I used "tuple unpacking" to swap elements
            # we could alternatively just use a "temp" variable to facilitate the swap
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            # Decrement j by 1
            j -= 1
    # Return the list
    return nums


# --------------------------------------------------


test = [1, 3, 2, 7, 4, 0, 1]
print(insertion_sort(test))
