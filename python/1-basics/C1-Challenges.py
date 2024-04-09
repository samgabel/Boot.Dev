def number_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

#-----------------------------------------------------

def main(a):
    func = number_sum(a)
    print(func)

#------------------------

test = (18)  #171
main(test)
