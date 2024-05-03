# Building on from our Stack Class we created, lets now "Balance Parenthesis"



def is_balanced(input_str):
    stack = Stack()
    # Want to filter for only the "()" chars
    for char in input_str:
        # Push all "(" to stack
        if char == "(":
            stack.push(char)
        # For every occurence of ")" we want to pop(), if there are more ")" than "(" then we are unbalanced
        if char == ")":
            if stack.pop() is None:
                return False
    # If we have a balanced set of parenthesis in the input_str then the stack should, at this point, be empty
    return stack.peek() is None


# don't modify below this line


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



# --------------------------------



test = "()()"
test2 = "(the quick brown)fox(jumps over the lazy)dog)"
test3 = "(()))"
test4 = "()("
test5 = ")("
print(f"{test} ->", is_balanced(test))
# True
print(f"{test2} ->", is_balanced(test2))
# False
print(f"{test3} ->", is_balanced(test3))
# False
print(f"{test4} ->", is_balanced(test4))
# False
print(f"{test5} ->", is_balanced(test5))
# False
