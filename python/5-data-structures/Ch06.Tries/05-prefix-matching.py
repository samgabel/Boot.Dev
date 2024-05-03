# Implement a method to return all possible words in the trie that start with an input prefix.

# Time Complxity:
# O(k + m) ->
    ## Searching for the prefix in the trie takes O(k) time because we need to traverse k nodes in the trie,
    ## one for each character in the prefix.
    ## Once reaching the node representing the end of the prefix, we need to traverse all of the leaf nodes
    ## under that node, taking O(m) time, where m is the number of matching words.



class Trie:
    def words_with_prefix(self, prefix):
        words = []
        current = self.root
        # drill down to the layer of the trie where the prefix ends
        for letter in prefix:
            if letter not in current:
                return []
            current = current[letter]
        # at the last layer we call `search_level`
        return self.search_level(current, prefix, words)

    def search_level(self, cur, cur_prefix, words):
        # append any comlete word we find, to our `words` list, for any call in our call stack
        if self.end_symbol in cur:
            words.append(cur_prefix)
        # recursively search for complete words
        # sorted helps us print out our `words` list in the order they appear in the trie
        for key in sorted(cur.keys()):
            if key != self.end_symbol:
                # make sure to advance our current level and current prefix
                self.search_level(cur[key], cur_prefix + key, words)
        return words


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
result.add("bad")
result.add("back")
result.add("bat")

pre = "ba"
print(f"The prefix '{pre}' has the words: {result.words_with_prefix(pre)}\n")

print(json.dumps(result.root, sort_keys=True, indent=4))

