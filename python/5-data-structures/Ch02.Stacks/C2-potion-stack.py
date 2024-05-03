# Override the .push() method in the PotionStack class.
# If the potion on the top of the stack is of the same type as the potion being pushed, then the push operation fails and nothing happens.
# Otherwise, use the .push() method of the Stack class to push the potion onto the stack.



class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]


# don't modify above this line


class PotionStack(Stack):
    def push(self, item):
        if self.peek() == item:
            return
        super().push(item)


# -----------------------------------------------


pouch = PotionStack()
pouch.items = ["healing", "armor", "mana"]
print(pouch.items)

# Mana is already top of the stack so it should fail to push "mana"
pouch.push("mana")
print(pouch.items)

# Armor is not top of the stack so it should succeed to puch "armor"
pouch.push("armor")
print(pouch.items)
