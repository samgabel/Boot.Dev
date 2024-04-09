def calculate_total(items_purchased, grocery_list):
    item_prices = {
        "milk": 2.50,
        "eggs": 3.25,
        "bread": 1.21,
        "cheese": 3.50,
        "apples": 7.44,
        "bananas": 3.88,
        "carrots": 3.89,
        "lettuce": 1.12,
        "potatoes": 32.21,
        "cereal": 5.99,
    }

    unpurchased_items = []  # names of items in grocerey_list not found in items_purchased
    reciept = {}  # dict of items_purchased => price
    total = 0  # total cost of all items puchased

    for item in grocery_list:
        if item not in items_purchased:
            unpurchased_items.append(item)

    for item in items_purchased:
        reciept[item] = item_prices[item]

    for item in reciept:
        total += reciept[item]

    return unpurchased_items, reciept, total


def main(a, b):
    func = calculate_total(a, b)
    print(func)

#----------------------------------------------------------

shop = [
    "milk",
    "eggs",
    "cheese",
    "apples",
    "bananas",
    "lettuce",
    "cereal",
]
want = [
    "milk",
    "oatmeal",
    "eggs",
    "cheese",
    "apples",
    "bananas",
    "carrots",
    "lettuce",
    "potatoes",
    "cereal",
    "chicken",
]

main(shop, want)
