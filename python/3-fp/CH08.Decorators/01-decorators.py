def file_type_aggregator(func_to_wrap):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        nonlocal counts

        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1

        result = func_to_wrap(doc, file_type)

        return result, counts

    return wrapper


@file_type_aggregator
def process_doc(doc, file_type):
    return f"Processing doc: {doc} with File Type: {file_type}"

# --------------------------------------------------------------------------------

print(process_doc("Hello", "txt"))
print(process_doc("World", "txt"))
print(process_doc("Heya", "md"))


### A Note:
# This higher order function is indeed unPure.
# The function is stateful because it houses a dictionary whose contents change, even given the same arguments
