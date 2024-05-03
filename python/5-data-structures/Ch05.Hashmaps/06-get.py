# Use the `key_to_index` method to find the correct index to lookup in the `self.hashmap` datastore
# if a value doesn't exist at that index, raise the following `Exception` to indicate no key was found



class HashMap:
    def get(self, key):
        # Use our hashing algorithm `.key_to_index` to generate our index from the key we want to search for
        i = self.key_to_index(key)
        bucket = self.hashmap[i]
        if bucket is None:
            raise Exception(f"Sorry, '{key}' not found")
        # We only want the value to be returned, not the whole tuple stored in the bucket
        return bucket[1]


    # don't touch below this line


    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def insert(self, key, value):
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)

    def __init__(self, size):
        self.hashmap: list[None | tuple] = [None for _ in range(size)]

    def __repr__(self):
        final = ""
        for t in self.hashmap:
            if t != None:
                final += f" - {str(t)}\n"
        return final


# --------------------------------------------------------------------------------------------------


# there will be collisions so "apple" and "banana" wil be overriden by their later counterparts
valkey = [("javascript", 4), ("c", 6), ("golang", 1), ("python", 2), ("c++", 7), ("java", 3), ("rust", 5)]

h = HashMap(512) # seems like there is a conflict with "python" in smaller arrays of buckets: 512 seems to inlcude all
print(f"For a hash map with size: {len(h.hashmap)}\n")
for p in valkey:
    h.insert(p[0], p[1])
print(h)

# Printing the `.get` method
try:
    a = "python"
    print(f"Getting the value at '{a}' ->", h.get(a))
    b = "haskell"
    print(f"Getting the value at '{b}' ->", h.get(b))
except Exception as e:
    print(e)
