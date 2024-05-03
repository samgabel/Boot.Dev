# In our previous `HashMap` iterations, we have a lot of collisions because we are using a fixed size for our hashmap.
# To reduce the chances of collisions, we can increase the number of slots in our hashmap (resizing).
# We create a new hashmap with a larger number of slots, then we re-insert all the key-value pairs from the old hashmap to the new one.



class HashMap:
    def insert(self, key, value):
        # Modified `insert` method
        self.resize()
        # -----------------------
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        """
        Resets and resizes the hash table, and calls the `insert` for each preexisting key->value to be reinserted into the new hash table
        """
        # Creates a hash table of size 1 (None) if the size is 0
        if len(self.hashmap) == 0:
            self.hashmap = [None]
        # Resets the current hash table and resizes it to 10 times the original size if our precentage from `current_load` is less than 5%
        # then repopulates the new hash table with any preexisting values using the `insert` method
        cload = self.current_load()
        if cload >= 0.05:
            tmp_hashmap = self.hashmap
            self.hashmap = [None for _ in range(len(self.hashmap) * 10)]
            for bucket in tmp_hashmap:
                if bucket:
                    self.insert(bucket[0], bucket[1])

    def current_load(self):
        """
        Returns the number of filled buckets in the hashmap as a percentage of the total number of buckets
        """
        # If the length of the underlying list is zero, return `1`
        if len(self.hashmap) == 0:
            return 1
        # Otherwise, return the percentage of the number of key->value pairs to total size of the hash table
        count = 0
        for bucket in self.hashmap:
            if bucket:
                count += 1
        return count / len(self.hashmap)


    # don't touch below this line


    def __init__(self, size):
        self.hashmap: list[None | tuple] = [None for _ in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def get(self, key):
        # Use our hashing algorithm `.key_to_index` to generate our index from the key we want to search for
        i = self.key_to_index(key)
        bucket = self.hashmap[i]
        if bucket is None:
            raise Exception(f"Sorry, '{key}' not found")
        # We only want the value to be returned, not the whole tuple stored in the bucket
        return bucket[1]

    def __repr__(self):
        final = ""
        for t in self.hashmap:
            if t != None:
                final += f" - {str(t)}\n"
        return final


# --------------------------------------------------------------------------------------------------


valkey = [("javascript", 4), ("c", 6), ("golang", 1), ("python", 2), ("c++", 7), ("java", 3), ("rust", 5)]

h = HashMap(0)
print(f"Initializing with hashmap size: {len(h.hashmap)}\n")

for p in valkey:
    h.insert(p[0], p[1])
print(h)

print(f"Final hashmap size after insertions: {len(h.hashmap)}\n")

# If we try to find "javascript", we will get an error because there was a collision
# this means our hashing function isn't really that good, and our resizing method doesn't work for all cases
print("If we try to find 'javascript':")
try:
    print(h.get("javascript"))
except Exception as e:
    print(e)
