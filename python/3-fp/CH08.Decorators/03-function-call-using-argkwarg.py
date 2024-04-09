# TODO: revisit
## this section was tough becuase I didn't know how to iterate through args and kwargs (really didn't know that kwargs are stored in dicts)

def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        converted_args = []
        converted_kwargs = {}

        # Need to iterate thorugh each argument and apply the `conver_md_to_txt()` before passing back to `func()`
        for arg in args:
            converted_args.append(convert_md_to_txt(arg))

        # Need to retain the dictionary format for the kwargs (when we convert the values) in order to correctly pass them to the `func()`
        ### Notice at the bottom of the page, the arguments are kwargs
        for key, value in kwargs.items():
            converted_kwargs[key] = convert_md_to_txt(value)

        return func(*converted_args, **converted_kwargs)

    return wrapper


def convert_md_to_txt(doc):
    new_list = []

    for line in doc.split("\n"):
        new_list.append(line.lstrip(" #"))

    new_string = "\n".join(new_list)

    return new_string


# Don't edit below this line


@markdown_to_text_decorator
def concat(first_doc, second_doc):
    return f"""First: {first_doc}
Second: {second_doc}
"""


@markdown_to_text_decorator
def format_as_essay(title, body, conclusion):
    return f"""Title: {title}
Body: {body}
Conclusion: {conclusion}
"""



#---------------------------------------------------------------------



# concat()
doc1 = "# We like to play it all"
doc2 = "## Welcome to Tally Hall"

print(concat(doc1, doc2))

print("--------------------------------")

# format_as_essay()
t = "Why Python is Great"
c = "## That's why Python is great!"
b = """Python is a great language.

## Reasons:
* It's really easy to learn
* Everyone uses it
"""

print(format_as_essay(body=b, conclusion=c, title=t))
