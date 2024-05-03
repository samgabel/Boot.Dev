# Create methods called `min` and `max` in order to find the "min" and "max" values of the Binary Tree


class BSTNode:
    def get_min(self):
        # This example uses recursion
        if not self.left:
            return self.val
        return self.left.get_min()

    def get_max(self):
        # This example uses an iterative approach
        current = self
        while current.right:
            current = current.right
        return current.val


    # don't touch below this line


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
        if self.val == val:
            return
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return
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


# Print the tree structure
print(f"     {n}")
print("    / \\")
print(f"   {n.left}   {n.right}")
print("  / \\   \\")
print(f" {n.left.left}   {n.left.right}   {n.right.right}") # pyright: ignore

# Print the min and max of the tree
print()
print("Min:", n.get_min())
print("Max:", n.get_max())
