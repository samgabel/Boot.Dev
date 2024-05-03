# Create a method called `delete` in order to "delete" values into the Binary Tree


class BSTNode:
    def delete(self, val):
        if not self.val:
            return
        # Check to see if the val to delete is smaller than the current node val
        if val < self.val:
            if self.left:
                # we assign the node to the return of the recursive call in order to replace/delete the node
                self.left = self.left.delete(val)
            return self
        # Check to see if the val to delete is larger than the current node val
        if val > self.val:
            if self.right:
                # we assign the node to the return of the recursive call in order to replace/delete the node
                self.right = self.right.delete(val)
            return self
        # If this node is our target node
        if val == self.val:
            # These two are base cases for the below recursive call
            if not self.right:
                return self.left
            if not self.left:
                return self.right
            # If there are nodes on either side of the target node
            min_larger_node = self.right
            # We want to find the smallest value on the target node right branch because it is the next value after we delete the target value
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            self.val = min_larger_node.val
            # we assign the node to the return of the recursive call in order to replace/delete the node
            self.right = self.right.delete(min_larger_node.val)
        return self


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

#      5                   7
#     / \                 / \
#    3   7               3   8
#   / \   \             / \
#  2   4   8           2   4

print("Original Tree", "\n")
print(f"     {n}")
print("    / \\")
print(f"   {n.left}   {n.right}")
print("  / \\   \\")
print(f" {n.left.left}   {n.left.right}   {n.right.right}") # pyright: ignore

print("\nNode to delete: 5")
n.delete(5)
print()

print(f"     {n}")
print("    / \\")
print(f"   {n.left}   {n.right}")
print("  / \\")
print(f" {n.left.left}   {n.left.right}") # pyright: ignore

