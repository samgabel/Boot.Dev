# Implement the `search_range` method for the `BSTNode` class.
# The method should take two arguments, and return a list of values that fall within the specified range, inclusive.



class BSTNode:
    def search_range(self, lower_bound, upper_bound):
        existing_nodes = []
        # when we find a value that meets our criterea we want to append it to the `existing_nodes` list (for that particular recursive call)
        if self.val and lower_bound <= self.val <= upper_bound:
            existing_nodes.append(self.val)
        # we keep recursing down the left side until the criterea is no longer met
        if self.left and self.val > lower_bound:
            left = self.left.search_range(lower_bound, upper_bound)
            # we extend up the call stack
            existing_nodes.extend(left)
        # we keep recursing down the right side until the criterea is no longer met
        if self.right and self.val < upper_bound:
            right = self.right.search_range(lower_bound, upper_bound)
            # we extend up the call stack
            existing_nodes.extend(right)
        return existing_nodes


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


l = 2
u = 6
print(f"\nWithin the range {l} to {u} (traverse-preorder):", n.search_range(l, u))
