# TODO: revisit
## need a better understanding on *args **kwargs

def args_logger(*args, **kwargs):
    args_tuple = args

    # using `sorted()` on a dict turns it into a list of just the keys
    # we need to use the `.items()` method in order to return a tuple (key, pair)
    # then we need to specify what our `key` parameter is, in this case we could have omitted this bc it is the first value in the tuple
    kwargs_sorted = sorted(kwargs.items(), key=lambda x: x[0])

    # we are actually just iterating through `args`
    for a in args_tuple:
        print(f"* {a}")

    # we are actually just iterating through `kwargs.items()` which are also then sorted by `x[0]` (just the first value in the dict)
    for k in kwargs_sorted:
        print(f"* {k[0]}: {k[1]}")


#---------------------------------------------------------------------


def test(*args, **kwargs):
    args_logger(*args, **kwargs)
    print("========================================")


def main():
    test(1, 2, date_str="01/01/2023")
    test(message="Hello World", to_delete="l")
    test(1, 2, 3, 4, 5)
    test("hi", True, name="Lane", age=28)


main()
