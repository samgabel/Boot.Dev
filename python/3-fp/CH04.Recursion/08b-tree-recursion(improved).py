def list_files(current_node, current_path = ""):

    # instantiate list to be returned after recursion unwind
    path = []

    # looping through the nested dictionarioes
    for node in current_node:

        # our current full path for this iteration
        current_r_dest = f"{current_path}/{node}"
        # our current *value* for this iteration (used to get next dictionary in subsequent recursive calls)
        node_values = current_node[node]

        if node_values is None:
            path.append(current_r_dest)
        else:
            path.extend(list_files(node_values, current_r_dest))

    return path


#-----------------------------------------------------------------------------------------------


nested = {
    "Documents": {
        "Proposal.docx": None,
        "Report": {"AnnualReport.pdf": None, "Financials.xlsx": None},
    },
    "Downloads": {"picture1.jpg": None, "picture2.jpg": None},
}

print(list_files(nested))

# path = [
#     "/Documents/Proposal.docx",
#     "/Documents/Report/AnnualReport.pdf",
#     "/Documents/Report/Financials.xlsx",
#     "/Downloads/picture1.jpg",
#     "/Downloads/picture2.jpg",
# ]

