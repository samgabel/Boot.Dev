def remove_nonints(nums):
    clean = []
    for num in nums:
        if type(num) == int:
            clean.append(num)
    return clean

#-----------------------------------------------------

def main(a):
    func = remove_nonints(a)
    print(func)

#------------------------

test = [1, "your mom gay", False, 4, 9, 9, 18]
main(test)
