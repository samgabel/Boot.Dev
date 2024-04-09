def divide_list(nums, divisor):
    new_list = []
    for num in nums:
        float_value = float(num / divisor)
        new_list.append(float_value)
    return new_list
#-----------------------------------------------------

def main(a, b):
    func = divide_list(a, b)
    print(func)

#------------------------

test = [15, 30, 45]
divide = 3

main(test, divide)
