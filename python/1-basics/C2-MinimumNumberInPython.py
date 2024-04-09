def find_min(nums):
    min_so_far = float("inf")
    for num in nums:
        if num < min_so_far:
            min_so_far = num
    return min_so_far

#-----------------------------------------------------

def main(a):
    func = find_min(a)
    print(func)

#------------------------

test = [1, 2, 5, 4, 9, 9, 18]  #171
main(test)
