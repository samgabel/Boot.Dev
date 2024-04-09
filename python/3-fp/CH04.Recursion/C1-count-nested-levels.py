# REVISIT

def count_nested_levels(nested_documents, target_document_id, level=1):
    for doc in nested_documents:
        # Base Case
        if doc == target_document_id:
            return level

        # Recursive return set to "next" variable
        next = count_nested_levels(nested_documents[doc], target_document_id, level+1)

        # If a deeper nested recursive return is found, then immediately return next
        if next != -1:
            return next

    # Default recursive return if base case not found
    return -1

#---------------------------------------------------------------------------

nest = {
    1: {
        3: {},
        2: {
            5: {}
        },
    }
}

print(count_nested_levels(nest, 3))
