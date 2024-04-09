# NOTE: This is tricky

def markdown_to_text(doc_content):
    heading_removed = list(map(lambda x: x.lstrip("# "), doc_content.split("\n")))
    astericks_removed = remove_astericks_from_words(heading_removed)
    return "\n".join(astericks_removed)

def remove_astericks_from_words(doc_list):
    no_asterick_list = []

    new_list = doc_list.copy()
    for line in new_list:
        # this conditional reduces the amount of looping for [words in line] => which is much more taxing
        # maybe this bullshitass code might be better because of algorithmic efficiency?
        if line.count("*") > 1:
            new_line = []
            for word in line.split():
                if len(word) > 1:
                    new_line.append(word.strip("*"))
                else:
                    new_line.append(word)
            no_asterick_list.append(" ".join(new_line))
        else:
            no_asterick_list.append(line)

    return no_asterick_list


#----------------------------------------------------------------------------------------------------


md = """
# Hash header #

*Italics line*
**Bold line**

## Subheader

* List item
* *Italics list item*
* **Bold list item**
"""

print(markdown_to_text(md))
