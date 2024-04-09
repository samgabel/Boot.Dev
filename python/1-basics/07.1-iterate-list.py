def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # for i in range(0, len(items)):
    #     if items[i] == "Potion":
    #         potion_count += 1
    #     if items[i] == "Bread":
    #         bread_count += 1
    #     if items[i] == "Shortsword":
    #         shortsword_count += 1
    for item in items:
        if item == "Potion":
            potion_count += 1
        if item == "Bread":
            bread_count += 1
        if item == "Shortsword":
            shortsword_count += 1

    return potion_count, bread_count, shortsword_count

num_of_potions, num_of_bread, num_of_shortsword = get_item_counts(["Bread", "Potion", "Shortsword", "Potion"])
print(num_of_potions, num_of_bread, num_of_shortsword)
