# Create a method called `insert` in order to "insert" values into the Binary Tree


class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def __repr__(self):
        return f"{self.val}"

    def insert(self, val):
        if not self.val:
            self.val = val
            return
        # Skip if inserting value is already equal to the current node value
        if self.val == val:
            return
        # If our insert value is less than the node value and...
        # if there is already a value on the left, recurse til we find our correct spot
        # if there is no value on the left, create a new node object and assign it to the left
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return
        # If our insert value is greater than the node value and...
        # if there is already a value on the right, recurse til we find our correct spot
        # if there is no value on the right, create an new node object and assign it to the right
        if val > self.val:
            if self.right:
                self.right.insert(val)
                return
            self.right = BSTNode(val)
            return



# ---------------------------------------------------------------------------------------------------



n = BSTNode(5)
n.insert(3)
n.insert(7)
n.insert(8)
n.insert(2)
n.insert(4)

#      5
#     / \
#    3   7
#   / \   \
#  2   4   8


print(f"     {n}")
print("    / \\")
print(f"   {n.left}   {n.right}")
print("  / \\   \\")
print(f" {n.left.left}   {n.left.right}   {n.right.right}") # pyright: ignore
