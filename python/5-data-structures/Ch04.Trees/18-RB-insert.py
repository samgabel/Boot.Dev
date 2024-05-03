# Currently this is not the full self balancing implementation of a RB Tree...
# At this stage we do not have rotations and recoloring so the tree is currently unbalanced and uncolored.

# The "raw" insert is very close to the insert method that we used for BST
# An exception is that we need to carry reference to the parent node




class RBNode:
    def __init__(self, val):
        self.red: bool = False
        self.parent: None | RBNode = None
        self.val: int = val
        self.left: None | RBNode = None
        self.right: None | RBNode = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil


    # don't touch above this line

# pyright: reportOptionalMemberAccess = false

    def insert(self, val):
        # CREATE THE NEW NODE
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True
        # FIND THE PARENT OF THE NEW_NODE
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate val, just ignore
                return
        # INSERT THE NEW NODE
        new_node.parent = parent
        if parent is None:
            # this is what is executed on our first insert with no root node
            # allows us to set our root node and run the while loop above
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node



# ---------------------------------------------------------------------------------------------------



n = RBTree()
n.insert(5)
n.insert(3)
n.insert(7)
n.insert(8)
n.insert(2)
n.insert(4)


# This is an incomplete version of the RB Tree
# Notice how it still looks like a BST (except each node carries additional metadata)
# We now need to implement rotations and recoloring

#           5R
#         /    \
#       3R      7R
#      /  \    /  \
#    2R   4R  B   8R
#   / \  / \      / \
#   B B  B B      B B


print(f"         {n.root.val}R")
print("       /    \\")
print(f"     {n.root.left.val}R      {n.root.right.val}R")
print("    /  \\    /  \\")
print(f"  {n.root.left.left.val}R   {n.root.left.right.val}R  B    {n.root.right.right.val}R")
print(" / \\  / \\       / \\")
print(" B B  B B       B B")

