import functools


def accumulate(doc, sentence):
    return doc + ". " + sentence


def accumulate_first_sentences(sentences, n):
    if not sentences or n < 1:
        return ""
    return functools.reduce(accumulate, sentences[:n]) + "."


#------------------------------------------------

lst = ["The world is changed", "I feel it in the water", "I feel it in the earth"] 
num = 3

print(accumulate_first_sentences(lst, num))
