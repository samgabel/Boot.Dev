def double_string(string):
    complete = ""

    for char in string:
        complete += char * 2

    return complete


def main(a):
    func = double_string(a)
    print(func)

#---------------------------------------------

sentence = "The quick brown fox"

main(sentence)
