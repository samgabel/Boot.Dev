def list_files(current_node, current_path = ""):

    file_paths = []

    for node in current_node:
        # if we encounter a full path
        if current_node[node] is None:
            file_paths.append(f"{current_path}/{node}")
        # recurse here
        else:
            current_rec_path = current_path + "/" + f"{node}"
            # some work needs to be done in understanding the .extend() method
            # how are we able to add to the list even through recursive calls?
            file_paths += list_files(current_node[node], current_rec_path)

    return file_paths



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
