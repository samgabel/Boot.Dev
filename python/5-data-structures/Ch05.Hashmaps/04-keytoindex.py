# We'll almost always just use a language's built in implementation of a hash map (ie: dictionary -> python, unordered_map -> C++)
# To illustrate what's going on under the hood...
    ## we will build our a class called `HashMap`
    ## and use a python list underneath to store data in an instance variable called `hashmap`
    ## we are implementing the hash map to the `size` provided

# Notice that there is a collision between "7" and "javascript"



class HashMap:
    def key_to_index(self, key):
        sum = 0
        for c in key:
            # `ord()` function takes a string char as input and outputs it's equivalant unicode number
            sum += ord(c)
        # we take the sum of the unicode characters for each key, and modulo the size of the hash table givng us the index (idx)
        # the issue with this is we can get collisions when...
            ## key strings sum up to greater than two times the size of the hash table (wrap around) (ie: 1079 % 512 = 55)
            ## key strings sum up to identical sums as other keys
        idx = sum % len(self.hashmap)
        # we really only want the index, but I am showing the sum as well to show collisions ("javascript" & "7")
        return idx, sum


    # don't touch below this line


    def __init__(self, size):
        self.hashmap = [None for _ in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)


# --------------------------------------------------------------------------------------------------


keys = ["golang", "python", "java", "javascript", "7", "rust", "c", "c++"]
# 512 refers to the `size` property or the number of "buckets" or "slots" available in the hash map for storing data
h = HashMap(512)
print(f"For a hash map with size: {len(h.hashmap)}\n")
for key in keys:
    print(f'"{key}" hashes to (index, sum) ->', h.key_to_index(f"{key}"))
