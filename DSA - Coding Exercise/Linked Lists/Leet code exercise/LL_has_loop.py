class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # WRITE HAS_LOOP METHOD HERE #
    #                            #
    #                            #
    #                            #
    #                            #
    ##############################

    def has_loop(self):
        slow = self.head                                    # setting slow move by 1
        fast = self.head                                    # settng fast move by 2

        while fast is not None and fast.next is not None:   # if fast is none then it is end of loop
            slow = slow.next                                # move by 1
            fast = fast.next.next                           # move by 2

            if slow == fast:                                # if they are crossover again then loop is exist
                return True
        return False                                        # if not crossover then no loop

    
    
    
    
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True




my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) # Returns False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""
