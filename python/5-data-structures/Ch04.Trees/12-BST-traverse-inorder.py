# Create a method called `inorder` in order to "list" the values in the binary tree: smallest -> greatest


class BSTNode:
    def inorder(self, visited):
        # Traverse to deepeset node on the left branch
        if self.left:
            self.left.inorder(visited)
        # Start by appending the deepest left branch (containing no further left or right nodes)
        visited.append(self.val)
        # 1 function call up from the deepest stack layer, we will create a function call for the right node
        if self.right:
            self.right.inorder(visited)
        return visited


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


print("\nList in-order:", n.inorder([]))

