# Know as the "Subset Sum Problem" (NP-hard) ->
# It should take a list of integers nums and an integer target, and return True if there exists a subset of nums that adds up to target, and False otherwise.



def subset_sum(nums, target):
    return find_subset_sum(nums, target, len(nums) - 1)


def find_subset_sum(nums, target, index):
    if target == 0:
        return True
    if index < 0 and target != 0:
        return False
    # If we run into a number in the array that is larger than our target then we want to skip it and move on the the next index
    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)
    # Both recursive calls work in tandem with one another to "loop" through each index
    # and find all combos or (subsets) of numbers that add into the target
    res = find_subset_sum(nums, target, index - 1)
    # Here we do the same as above, but we subtract that "addend" from the target sum for each new index
    # This allows us to see if there are any combination of numbers equal to the target
    res2 = find_subset_sum(nums, target - nums[index], index - 1)
    # Since the recursive calls will end in a boolean we can just return the values of the recursive calls
    return res or res2


# -------------------------------------------------------------------



list_nums = [3, 34, 4, 12, 5, 2]
target_int = 9
print(subset_sum(list_nums, target_int))
# True
