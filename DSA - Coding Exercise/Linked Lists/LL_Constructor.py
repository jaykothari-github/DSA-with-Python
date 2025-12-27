class Node:

    def __init__(self, value):
        self.value = value      # assign the value of the node
        self.next = None        # initialize the next pointer to None

  
class LinkedList:

    def __init__(self, value):
        new_node = Node(value)      # create a new node with the given value
        self.head = new_node        # set head to the new node
        self.tail = new_node        # set tail to the new node
        self.length = 1             # initialize length to 1


my_linked_list = LinkedList(4)   # Create a new linked list with an initial value of 4

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)



"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    