# Implement a method to search and return all of the substrings found in the document also found in the trie.

# Time Complexity:
# O(n * m) ->
    ## Where n is the length of the document and m is the depth of the trie.



class Trie:
    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                char = document[j]
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
result.add("bad")
result.add("baddie")
result.add("badguy")
result.add("suck")

text = "the badguy really sucks"
print(f"For the text '{text}' the bad words found are:\n{result.find_matches(text)}\n")

print(json.dumps(result.root, sort_keys=True, indent=4))

