def lines_with_sequence(char):

    def with_char(length):
        sequence = char * length

        def with_length(doc):
            nonlocal sequence
            count = 0
            lines = doc.split("\n")
            for line in lines:
                if sequence in line:
                    count += 1

            return count

        return with_length

    return with_char


# -------------------------------------------------


char = "a"
length = 2
doc = '''
aaaa*
aabb*
abbb
accc
addd
abcd
aaax*
'''

print("Input:\n", f" * char: {char}\n", f" * length: {length}\n", f" * doc: {doc}", "\n")
print(f"Given the input doc, there are {lines_with_sequence(char)(length)(doc)} three lines with '{char * length}'")
