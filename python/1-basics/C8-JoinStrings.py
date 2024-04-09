def join_strings(strings):
    sentence = ""
    for string in strings:
        sentence += string + ","
    if len(sentence) != 0:
        sentence = sentence[:-1]
    return sentence

#-----------------------------------------------------

def main(a):
    func = join_strings(a)
    print(func)

#------------------------

test = ["hello", "world", "!"]
main(test)
