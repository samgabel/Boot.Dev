def converted_font_size(font_size):

    def inner_func(doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("Invalid doc type")

    return inner_func


# --------------------------------------------


font_size = 12
new_doc_type = "md"

print("Inputs:\n", f" * font_size: {font_size}\n", f" * doc_type: {new_doc_type}\n")
print("New font size is now:", converted_font_size(12)("md"))
# converted_font_size(12) will return a function that will accept ("md") as input
