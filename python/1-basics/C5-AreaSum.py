def area_sum(rectangles):
    total = 0
    for rectangle in rectangles:
        area = rectangle["height"] * rectangle["width"]
        total += area
    return total

#-----------------------------------------------------

def main(a):
    func = area_sum(a)
    print(func)

#------------------------

test = [
    { # 30
        "height": 5,
        "width": 6
    },
    { # 18
        "height": 2,
        "width": 9
    },
    { # 100
        "height": 1,
        "width": 100
    }
]

main(test)
