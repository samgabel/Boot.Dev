def reverse_string(s):

    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])


#-----------------------------------------------------------------------


string = "Python"

print(reverse_string(string))
