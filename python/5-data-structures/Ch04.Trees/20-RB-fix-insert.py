# With this final method `fix_insert`, we will fix the previous iterations of RB Tree methods.
# When we are done we should have a fully functional RB Tree (albeit insert-only)



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

# pyright: reportOptionalMemberAccess = false

    def rotate_left(self, x):
        if x == self.nil or x.right == self.nil:
            return
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x == self.root:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        elif x == x.parent.right:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        if x == self.nil or x.left == self.nil:
            return
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x == self.root:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        elif x == x.parent.right:
            x.parent.right = y
        y.right = x
        x.parent = y



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

        self.fix_insert(new_node) # Call the new function


    # dont touch above this line
    # TODO: make sense of this code below and annotate


    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:

            if new_node.parent == new_node.parent.parent.right:
                uncle = new_node.parent.parent.left
                if uncle.red:
                    uncle.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                elif not uncle.red:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)

            elif new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                if uncle.red:
                    uncle.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                elif not uncle.red:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)

        self.root.red = False



# ---------------------------------------------------------------------------------------------------

# Insert Tree
n = RBTree()
n.insert(1)
n.insert(2)
n.insert(3)
n.insert(4)
n.insert(5)
n.insert(6)
n.insert(7)


# Print BST Implementation
print("Binary Search Tree:\n")
print(">1\n  >2\n    >3\n      >4\n        >5\n          >6\n            >7")


# Print RB Tree Implementation
def pn(node):
    if node.red == True:
        return f"{node.val}R"
    else:
        return f"{node.val}B"

n1 = n.root
n2 = n.root.left
n3 = n.root.right
n4 = n.root.right.left
n5 = n.root.right.right
n6 = n.root.right.right.left
n7 = n.root.right.right.right

print("\nRed-Black Tree:\n")
print(f"     {pn(n1)}")
print("    /  \\")
print(f"  {pn(n2)}    {pn(n3)}")
print("       /  \\")
print(f"     {pn(n4)}    {pn(n5)}")
print("          /  \\")
print(f"        {pn(n6)}    {pn(n7)}")

