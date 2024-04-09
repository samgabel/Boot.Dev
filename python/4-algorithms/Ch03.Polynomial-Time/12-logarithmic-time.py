# a binary search function is in logarithmic time
# return True if target is found, False if not


def binary_search(target, arr):
    l: int = 0
    r: int = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if target < arr[mid]:
            r = mid - 1
        elif target > arr[mid]:
            l = mid + 1
        else:
            return True

    return False


#--------------------------------------------------------------


sorted_list = [1, 2, 3, 4, 7, 8, 9, 11, 12]
print(binary_search(9, sorted_list))
