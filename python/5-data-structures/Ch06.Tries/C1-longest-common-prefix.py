# Implement a method to find the longest common prefix of the Trie data structure.

# Time Complexity:
# O(L) ->
    ## We define L as the length of the longest word in the trie.



class Trie:
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        # loop only to be broken by a break statement
        while True:
            # we want to grab all of the children keys so long as they are not `end_symbol`
            children = []
            # we need to store the end_symbols as well in order to determine when a word is ending
            # this way if a word ends and we only have 1 other key, we don't continue (ie: bed, bedroom) -> words that are subsets of others
            word_end = []
            for key in current.keys():
                if key == self.end_symbol:
                    word_end.append(key)
                else:
                    children.append(key)
            # if there is only 1 key in the current level we can keep drilling down, and add the key to `prefix`
            # also want to check that we don't have any words ending, bc if we do, we should not append anymore to `prefix`
            if len(children) == 1 and len(word_end) < 1:
                child = children[0]
                prefix += child
                current = current[child]
            # if there are multiple or no keys in the level then we are done
            else:
                break
        return prefix


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
result.add("be")
result.add("bed")
result.add("bedroom")

print(f"The longest common prefix in this trie is: {result.longest_common_prefix()}\n")

print(json.dumps(result.root, sort_keys=True, indent=4))

