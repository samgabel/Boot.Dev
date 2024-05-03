class Stack:
    def __init__(self):
        self.arrows = []

    def push(self, arrow):
        self.arrows.append(arrow)

    def pop(self):
        if self.arrows:
            return self.arrows.pop()
        return None

    def peek(self):
        if self.arrows:
            return self.arrows[-1]
        return None

    def size(self):
        return len(self.arrows)


# --------------------------------------------------------------


sling = Stack()
sling.arrows = ["normal", "normal", "normal", "normal"]
print(sling.arrows)
# PUSH
sling.push('poison')
print(f"Stack PUSH(poison):", sling.arrows)
# POP
print(f"Stack POP: {sling.pop()}", sling.arrows)
# PEEK
print(f"Stack PEEK: {sling.peek()} <-", sling.arrows)
# SIZE
print(f"Stack SIZE: {sling.size()}", sling.arrows)
