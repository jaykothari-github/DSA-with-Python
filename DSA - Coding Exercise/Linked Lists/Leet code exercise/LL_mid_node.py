class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        slow = self.head                    # Setting a slow point(move by 1 node)
        fast = self.head                    # Setting a fast point(move by 2 node)
        try:                                # when LL is even it throws error because of fast = fast.next.next
            while fast.next is not None:    # run until fast next is None
                slow = slow.next            # moving slow by 1
                fast = fast.next.next       # moving fast by 2
            else:
                return slow                 # after completing loop return slow for even LL
        except:
            return slow                     # when error throws it return slow (n//2 + 1 point)

    # def find_middle_node(self):
    #     slow = self.head
    #     fast = self.head
    #     while fast is not None and fast.next is not None:     # double condition to avoid error # condition order should be same
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""