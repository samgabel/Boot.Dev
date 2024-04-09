def remove_duplicates(lst):

    unique = set()
    for i in lst:
        unique.add(i)

    # turn set back into a list
    deduplicated = []
    # or just do deduplicated = list(unique)
    for i in unique:
        deduplicated.append(i)

    return deduplicated


def main(a):
    func = remove_duplicates(a)
    print(func)

#-------------------------------------------------------

games = [
    "Age of Empires",
    "World of Warcraft",
    "Halo",
    "Call of Duty",
    "Age of Empires",
    "Magic the Gathering",
    "Halo"
]

main(games)
