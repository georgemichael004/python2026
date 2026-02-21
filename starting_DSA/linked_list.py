class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            # This sets the next pointer to None, meaning that the new node does not yet point to any other node in the list. 
            # Later, next can be updated to point to another node to form the chain of a linked list.
            self.next = None

    def __init__(self):
        # This initializes a counter to track how many nodes (elements) are currently in the list.
        self.length = 0
        self.head = None # This initializes the head of the linked list to None, indicating that the list is initially empty.
    
    # You'll use this to keep track of how many nodes are in the list. So, with self.length == 0, it returns True, meaning that the list has no nodes.

    # If self.length is greater than 0, it returns False, meaning that the list has at least one node
    def is_empty(self):
        return self.length == 0

    def add(self, element):
        node = self.Node(element)
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1

    def remove(self, element):
        previous_node = None
        current_node = self.head
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        elif previous_node is not None:
            previous_node.next = current_node.next
        else:
            self.head = current_node.next
        self.length -= 1

my_list = LinkedList()
print(my_list.is_empty())

my_list.add(1)
my_list.add(2)
print(my_list.is_empty())
print(my_list.length)
