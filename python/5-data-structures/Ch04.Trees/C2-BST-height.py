# Complete the `height` method for the `BSTNode` class
# The `height` method should return the height of the tree rooted at the current node



class BSTNode:
    def height(self):
        left = 0
        right = 0
        if self.val is None:
            return 0
        if self.left:
            left = self.left.height()
        if self.right:
            right = self.right.height()
        # first we take the max between the two subtrees `left` and `right`, for that level in the call stack
        # then we take that value and add 1
        # as the call stack unwinds, only the largest value remains as we go up the call stack (or go up to the next parent node)
        return max(left, right) + 1


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

print(f"     {n}")
print("    / \\")
print(f"   {n.left}   {n.right}")
print("  / \\   \\")
print(f" {n.left.left}   {n.left.right}   {n.right.right}") # pyright: ignore


print(f"\nThe height of the tree is:", n.height())

