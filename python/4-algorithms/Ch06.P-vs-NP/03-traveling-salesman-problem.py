# Note: This is actually a Decision-TSP problem, not the original Optimization-TSP problem that is most commonly referenced
# therefore this is a NP-complete (bc of our `dist` constraint) not an NP-hard problem

# Complete the tsp function by performing a brute-force search using the provided algorithm.
# The brute-force search will, unfortunately, take factorial time, O(n!), because you will need to try all possible paths and keep track of the shortest.



def tsp(cities: list[int], paths: list[list[int]], dist: int) -> bool:
    """
    cities: a list of city identifiers (integers 0-n) -> to be fed into `permutations()` function to get a matrix of all permutations
    paths: a matrix where each point represents the distance between the two cities. ie: paths[cityA][cityB] holds the distance from cityA to cityB
    dist: the distance we are trying to find a path shorter than

    Returns 'True' if there is a path shorter than `dist`. 'False' otherwise.
    """
    # We need to make use of the `permutations()` function to make a matrix of all the city to city combinations
    cities_permutations = permutations(cities)
    # For each combination in that matrix...
    for cities_combo in cities_permutations:
        sum = 0
        # set cityA to be the previous city and cityB to the current (in our `citites_combo`)
        # query the `paths` matrix to get the length between cities and add that to the running `sum` for the current cities_combo iteration
        for i in range(1, len(cities_combo)):
            cityA = cities_combo[i - 1]
            cityB = cities_combo[i]
            sum += paths[cityA][cityB]
        # at the end of each cities_combo iteration, we see if the sum is less than our desired `dist`
        if sum < dist:
            return True
    return False


# don't touch below this line


def permutations(arr: list[int]) -> list[list[int]]:
    res = helper([], arr, len(arr))
    return res

def helper(res: list[list[int]], arr: list[int], n: int) -> list[list[int]]:
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res



# --------------------------------------------------------------------------------



city_list = [0, 1, 2, 3]
# actual path = 1, 2, 0, 3
paths_list = [
    [0, 988, 523, 497],
    [988, 0, 850, 940],
    [523, 850, 0, 802],
    [497, 940, 802, 0]
]
dist_int = 1877

print(tsp(city_list, paths_list, dist_int))
# True
