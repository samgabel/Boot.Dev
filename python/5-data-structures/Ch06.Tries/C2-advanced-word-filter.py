# Implement a better method to search and return all of the substrings with or without variations found in the document also found in the trie.

# Time Complexity:
# O(n * m) ->
    ## Where n is the length of the document and m is the depth of the trie.



class Trie:
    def advanced_find_matches(self, document, variations):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                char = document[j]
                if char in variations:
                    char = variations[char]
                if char not in level:
                    break
                level = level[char]
                if self.end_symbol in level:
                    matches.add(document[i:j + 1])
        return matches


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
result.add("darn")
result.add("sucks")
result.add("bad")

text = "This d@rn1t test with b@d words sucks!"
variations = {"@": "a", "1": "i", "4": "a", "!": "i",}
print(f"For the text '{text}' the bad words found are:\n{result.advanced_find_matches(text, variations)}\n")

print(json.dumps(result.root, sort_keys=True, indent=4))

