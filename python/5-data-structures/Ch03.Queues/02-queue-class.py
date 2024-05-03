class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if self.items:
            return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]

    def size(self):
        return len(self.items)


# ---------------------------------------------------


test = Queue()
test.items = [6, 5, 4, 3, 2, 1]
print(test.items)
# PUSH
test.push(7)
print(f"Stack PUSH(7):", test.items)
# POP
print(f"Stack POP: {test.pop()}", test.items)
# PEEK
print(f"Stack PEEK: {test.peek()} <-", test.items)
# SIZE
print(f"Stack SIZE: {test.size()}", test.items)

