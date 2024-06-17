def new_collection(initial_docs):
    defined_docs = initial_docs.copy()

    def inner_func(new_doc):
        nonlocal defined_docs
        defined_docs.append(new_doc)
        return defined_docs

    return inner_func


# ------------------------------------------------------


print("Initial documents list:", ["first_doc", "second_doc", "third_doc"], "\n")

appender = new_collection(["first_doc", "second_doc", "third_doc"])
print("Appending another doc:", appender("next_doc"))
