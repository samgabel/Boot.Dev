# Implement a method to add to the Trie data structure.
# The individual characters should make up the dictionary keys and the values should be dictionaries that store the next characters in the word(s)

# Time Complexity:
# O(m) ->
    ## `m` is the length of the word (in the context of the trie).
    ## It's about how many operations the method performs as it relates to the word's length.



class Trie:
    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True


    # don't touch below this line


    def __init__(self):
        self.root = {}
        self.end_symbol = "*"



# ----------------------------------------------------------------------------



import json

result = Trie()
result.add("be")
result.add("bad")
result.add("back")
result.add("bat")

print(json.dumps(result.root, sort_keys=True, indent=4))

