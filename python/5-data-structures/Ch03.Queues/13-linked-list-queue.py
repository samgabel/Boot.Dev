# The beauty of linked linsts is seen when applying a FILO technique (Queues)
# This is because instead of having to iterate and change each value of the queue to add to the queue, all we do is change the pointer to the next node

# Therefore...
## traditional `.insert()` method in a queue results in O(n) time
## linked list "relinking" in a queue results in O(1) time for adding and removing operations



class LLQueue:
    def __init__(self):
        self.tail = None
        self.head = None

    def remove_from_head(self):
        # If there is nothing to pop, then we want to return None
        if self.head is None:
            return
        # We need to replace our current head with the next value, our current head to be returned
        head_val = self.head
        self.head = self.head.next
        # If our new head is None that means our linked list is empty
        if self.head is None:
            self.tail = self.head
        # Return that stored head value from earlier
        return head_val

    def add_to_tail(self, node):
        # If there are no items in the linked list then we set the head nad tail to be the same node
        if self.head is None:
            self.head = node
            self.tail = node
            return
        # We set the current tail's pointer to be the node that we want
        self.tail.next = node # pyright: ignore[reportOptionalMemberAccess]
        # Now set the node to the new tail
        self.tail = node

# FOR PRINTING USE ONLY (NOT PART OF ACTUAL LINKED LIST OPERATION)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)

# -----------------------------------------------------------------

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return self.val



# ---------------------------------------------------------------------------------------------------------------



apple = Node("apple")
pear = Node("pear")
banana = Node("banana")
mango = Node("mango")
ll = LLQueue()


ll.add_to_tail(apple)
# apple
ll.add_to_tail(pear)
# apple <- pear
ll.remove_from_head()
# pear
ll.add_to_tail(banana)
# pear <- banana
ll.add_to_tail(mango)
# pear <- banana <- mango


# Time complexity stayed at O(1), for `.add_to_tail()` and `.remove_from_head*()` methods
print(ll)
