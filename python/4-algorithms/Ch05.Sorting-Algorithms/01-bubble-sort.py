# Bubble sort repeatedly steps through a slice and compares adjacent elements, swapping them if they are out of order. (sorts list in place)
# It continues to loop over the slice until the whole list is completely sorted.


def bubble_sort(nums: list[int]) -> list[int]:
    swapping = True
    end = len(nums)

    while swapping == True:
        swapping = False
        # after this for loop we will have the biggest value at the end of the list
        # hence the name "bubble sort" bc the "bubbles" float to the top
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                # we can swap values like this
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                # if swapping is not set to True at least once in the current iteration of the while loop...
                # then the while loop will end (and our list has no more reordering to be done)
                swapping = True
        # for each full iteration of the while loop we will remove the "bubble" from the next sequence
        end -= 1
    return nums


# This is time complexity: O((n-1) + (n-2) ... 2 + 1) -> O(n^2 / 2) -> O(n^2)
# at best it is O(n) if the list is already sorted it needs to go through a least 1 iteration
# upper bounds is O(n^2)


print(bubble_sort([5, 3, 7, 8, 7]))
# [3, 5, 7, 7, 8]
