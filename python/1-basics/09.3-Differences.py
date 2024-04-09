def find_missing_ids(first_ids, second_ids):
    new_list = []

    first_set = set()
    for id in first_ids:
        first_set.add(id)

    second_set = set()
    for id in second_ids:
        second_set.add(id)

    first_set -= second_set
    new_list = list(first_set)
    
    return new_list


def main(a, b):
    func = find_missing_ids(a, b)
    print(func)

#--------------------------------------------------------

first = [1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10]
secnd = [1, 2, 2, 3, 4, 5, 6, 7, 8]

main(first, secnd)
