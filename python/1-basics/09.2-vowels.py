def count_vowels(text):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    count = 0
    unique = set()

    for char in text:

        if char in vowels:
            count += 1
            unique.add(char)

    return count, unique


def main(a):
    func = count_vowels(a)
    print(func)

#----------------------------------------------------------

string = "Building a job-ready portfolio of coding projects does not happen overnight."

main(string)
