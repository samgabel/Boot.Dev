# Implement a method to check for the word in the Trie data structure.

# Time Complexity:
# O(m) ->
    ## In this case, we need to check each character of our input `word` against the tree, where the length of the `word` is m.



class Trie:
    def exists(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return self.end_symbol in current


    # don't touch below this line


    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"



# ----------------------------------------------------------------------------



import json

result = Trie()
result.add("hello")
result.add("help")
result.add("hi")

check = "help"
print(f"Is '{check}' in the trie: {result.exists(check)}\n")

print(json.dumps(result.root, sort_keys=True, indent=4))

