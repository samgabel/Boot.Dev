# remove duplicate items but retain order (can't use a set as our new list because it doesn't retain our order)
# only want to return the first *occurances* of values in our nums list


def remove_duplicates(nums: list) -> list:
    new_list = []
    # use a set of nums in order to create a comparison iterable
    unique_nums = set(nums)
    for num in nums:
        # our condition is that the num is still in our comparison set
        if num in unique_nums:
            # append to new_list
            new_list.append(num)
            # remove num from our comparision set
            unique_nums.remove(num)
        # condition to break loop is for our comparison set to be empty
        if len(unique_nums) == 0:
            break
    # this methodology allows us to save time with large lists because we only have
    # to iterate over our list until we have seen every num in our comparison set once
    # then we return our `new_list`
    return new_list


#----------------------------------------------------


l = [1, 2, 3, 5, 1, 3]
print(remove_duplicates(l))
# [1, 2, 3, 5]
