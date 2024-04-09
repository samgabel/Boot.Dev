def doc_format_checker_and_converter(conversion_function, valid_formats):


    def inner_func(filename, content):
        file_split = filename.split(".")

        if file_split[1] in valid_formats:
            return conversion_function(content)

        raise ValueError("Invalid file format")


    return inner_func


# Don't edit below this line -- these are the argument functions


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]


#----------------------------------------------------------------------------


formats_list = ["txt", "md", "doc"]

file = "sample.txt"
file_contents = "I really don't feel like screaming today."

#---------
# instantiate
result = doc_format_checker_and_converter(capitalize_content, formats_list)

try:
    # feed argument function
    print(result(file, file_contents))
except Exception as e:
    print(e)
