def remove_invalid_lines(document):
    return"\n".join(filter(lambda line: not line.startswith("-"), document.split("\n")))


#------------------------------------------------


string = "# The Plan\n- Phase 1\n- ???\n* Profit\nAny questions?\n"

print(remove_invalid_lines(string))
