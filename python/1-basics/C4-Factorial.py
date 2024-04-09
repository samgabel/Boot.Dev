def factorial(num):
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product

#-----------------------------------------------------

def main(a):
    func = factorial(a)
    print(func)

#------------------------

test = 6  #720
main(test)
