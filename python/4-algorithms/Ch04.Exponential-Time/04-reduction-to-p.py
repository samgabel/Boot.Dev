# make a fibonacci sequence function that is in time complexity of "P"
# for `slow_fib()` time complexity is O(2^n) which is an Exponential Time Complexity (very slow)


# this function is O(2^n)
# this function will never be able to calculate (n=100)
def slow_fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return slow_fib(n - 1) + slow_fib(n - 2)


# this function is O(n)
def fast_fib(n: int) -> int:
    # we need to hard-code the first current value + 2 generations back
    current = 0
    parent = 1
    grandparent = 0
    # indicate that the loop variable is not being used in the loop itself with "_"
    for _ in range(n):
        grandparent = parent
        parent = current
        current = parent + grandparent
    return current


#--------------------------------------------------


# print(fast_fib(20577)) # maximum fibonacci index in python (num has 4300 digits)
print(slow_fib(10))
