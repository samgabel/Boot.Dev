def purchase(price, money_available):
    if price > money_available:
        raise Exception("not enough money")
    return money_available - price

def main(a, b):
    try:
        func = purchase(a, b)
        print(func)
    except Exception as e:
        print(e)

#-----------------------------------------------------

wallet = 8
cost = 9

main(cost, wallet)
