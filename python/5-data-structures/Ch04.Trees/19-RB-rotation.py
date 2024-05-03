# Currently this is not the full self balancing implementation of a RB Tree...
# At this stage we do not have recoloring so the tree is uncolored.

# When rotating left:
    ## the "pivot" node's initial parent becomes it's left child
    ## the "pivot" node's old left child becomes it's initial parent's new right child

# Rotations are O(1) operations



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

    def rotate_left(self, x):
        # x = `A` node
        # Check to see if there is anything to rotate in the first place
        if x == self.nil or x.right == self.nil:
            return
        # Declare `y` as the pivot node `B`
        y = x.right
        # Make the left node of `B` now the right node of `A`
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        # This is where node `B` and `A` actually switch...
        y.parent = x.parent
        # if `A` is the root node of the tree then `B` will become the new root node
        if x == self.root:
            self.root = y
        # if `A` is it's parent node's left child then `B` will become the new left child
        elif x == x.parent.left:
            x.parent.left = y
        # if `A` is it's parent node's right child then `B` will become the new right child
        elif x == x.parent.right:
            x.parent.right = y
        # Update each `A` and `B` references in relation with one another
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        # x = `B` node
        # Check to see if there is anything to rotate in the first place
        if x == self.nil or x.left == self.nil:
            return
        # Declare `y` as the pivot node `A`
        y = x.left
        # Make the right node of `A` now the left node of `B`
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        # This is where node `A` and `B` actually switch...
        y.parent = x.parent
        # if `B` is the root node of the tree then `A` will become the new root node
        if x == self.root:
            self.root = y
        # if `B` is it's parent node's left child then `A` will become the new left child
        elif x == x.parent.left:
            x.parent.left = y
        # if `B` is it's parent node's right child then `A` will become the new right child
        elif x == x.parent.right:
            x.parent.right = y
        # Update each `B` and `A` references in relation with one another
        y.right = x
        x.parent = y


    # dont touch below this line


    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node



# ---------------------------------------------------------------------------------------------------

# Insert Tree
n = RBTree()
n.insert(5)
n.insert(3)
n.insert(7)
n.insert(8)


# Print Base Tree
print("Base Tree:\n")
print(f"      {n.root.val}R")
print("    /    \\")
print(f"  {n.root.left.val}R      {n.root.right.val}R")
print("            \\")
print(f"             {n.root.right.right.val}R")


# Rotated Left
#      5R             ->            7R
#    /    \           ->          /    \
#  3R      7R         ->        5R      8R
#         /  \        ->       /  \
#        B    8R      ->      3R   B

n.rotate_left(n.root)
print("\nRotate Left:\n")
print(f"          {n.root.val}R")
print("        /    \\")
print(f"      {n.root.left.val}R      {n.root.right.val}R")
print("     /    ")
print(f"   {n.root.left.left.val}R")


# Rotated Right
#        7R           ->          5R
#      /    \         ->        /    \
#    5R      8R       ->      3R      7R
#   /  \              ->             /  \
#  3R   B             ->            B    8R

n.rotate_right(n.root)
print("\nRotate Right:\n")
print(f"      {n.root.val}R")
print("    /    \\")
print(f"  {n.root.left.val}R      {n.root.right.val}R")
print("            \\")
print(f"             {n.root.right.right.val}R")

