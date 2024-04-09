def change_bullet_style(document):
    # # split document string into list of lines split at "\n"
    # list_doc = document.split("\n")
    # # feed iterable (list_doc) into convert_line() function to return iterator
    # changed_doc = map(convert_line, list_doc)
    # # .join() method concatenates all the lines in the iterator into a string, separating by "\n" 
    # joined_doc = "\n".join(changed_doc)
    # return joined_doc

    # all in 1 line ^
    return "\n".join(map(convert_line, document.split("\n")))


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line

#------------------------------------------------

string = "# The Plan\n- Phase 1\n- ???\n- Profit\nAny questions?\n"

print(change_bullet_style(string))
