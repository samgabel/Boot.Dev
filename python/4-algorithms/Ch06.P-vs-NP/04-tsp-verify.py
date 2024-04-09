# We know that "Decision-TSP" takes factorial time to solve (ie: for 4 cities that's 4! = 24 permutations), but it can be veryfied in "P" time
# Given the path we are trying to verify, is it actually smaller than our `dist` or distance we are trying a path shorter than?



def verify_tsp(paths, dist, actual_path):
    sum = 0
    # Sum up the distance between each city in the actual path
    for i in range(1, len(actual_path)):
        cityA = actual_path[i - 1]
        cityB = actual_path[i]
        sum += paths[cityA][cityB]
    # Return "True" if the sum actually is less than `dist`
    if sum < dist:
        return True
    return False



# ---------------------------------------------------------------------------



city_actual_list = [1, 2, 0, 3]
paths_list = [
    [0, 988, 523, 497],
    [988, 0, 850, 940],
    [523, 850, 0, 802],
    [497, 940, 802, 0]
]
dist_int = 1877
print(verify_tsp(paths_list, dist_int, city_actual_list))
# True
