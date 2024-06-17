def word_count_aggregator():
    count = 0

    def increment_count(doc):
        # when we have a nested function and want to access a variable in the outer function, we need to use the nonlocal keyword
        nonlocal count
        count += len(doc.split())
        return count

    return increment_count


# ---------------------------------------------------------


aggregator = word_count_aggregator()
print("The quick brown fox jumps over the lazy dog:", aggregator("The quick brown fox jumps over the lazy dog"))
print("Hello, world!:", aggregator("Hello, world!"))
