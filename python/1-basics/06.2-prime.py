def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# def main(a):
#     correct = is_prime(a)
#     print(correct)
#
# main(121)

print(is_prime(121))
