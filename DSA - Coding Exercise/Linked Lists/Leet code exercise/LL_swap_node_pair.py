class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result  
            
    def make_empty(self):
        self.head = None
        self.length = 0
 

        #   +===================================================+
        #   |               WRITE YOUR CODE HERE                |
        #   | Description:                                      |
        #   | - Swaps adjacent pairs of nodes in a singly linked|
        #   |   list by modifying the next pointers.            |
        #   |                                                   |
        #   | Parameters:                                       |
        #   | - None: Operates on the linked list's head.       |
        #   |                                                   |
        #   | Return:                                           |
        #   | - None: Modifies the linked list in place.        |
        #   |                                                   |
        #   | Behavior:                                         |
        #   | - If the list is empty or has one node, no swaps  |
        #   |   are performed.                                  |
        #   | - For each pair of adjacent nodes, swaps their    |
        #   |   positions by updating the next pointers.        |
        #   | - Uses a dummy node to simplify handling of the   |
        #   |   head node swap.                                 |
        #   | - Iterates through the list using a first pointer,|
        #   |   keeping the head unchanged until the final      |
        #   |   update.                                         |
        #   | - Sets the head to the new first node at the end. |
        #   +===================================================+

        ##### Steps of Below code #####

        # 1. Creating a dummy node 
        # 2. attached dummy node to head
        # 3. setting a var to set up tail point 
        # 4. creating 2 steps s1 and s2 with checking non empty LL 
        # 5. starting loop stating s1 and s2 are not none 
        # 6. swapping s1 and s2 
        # 7. changing previous point to s1
        # 8. checking pre.next exist and changing s1 point 
        # 9. checking s1.next exist and changing s2 point 
        # 10. if step 8 and 9 are not exist then breaking the loop
        # 11. Setting LL's new head point
        # 12. setting LL's tail point
        
    def swap_pairs(self):

        pre = Node(0)
        pre.next = self.head
        temp = pre
        s1 = self.head
        if s1:
            s2 = self.head.next

            # print(s2.next)
            while s1 and s2:
                s1.next = s2.next
                pre.next = s2
                s2.next = s1

                pre = s1    
                if pre.next: 
                    s1 = pre.next
                    if s1.next:
                        s2 = s1.next
                    else:
                        break
                else:
                    break
            
            self.head = temp.next
            
            run = self.head
            while run and run.next:
                run = run.next
            self.tail = run

#################################################3
       





# Test case 1: Swapping pairs in a list with an even number of nodes (1->2->3->4)
print("\nTest case 1: Swapping pairs in a list with an even number of nodes.")
ll1 = LinkedList(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
print("BEFORE: ", end="")
ll1.print_list()
print("AFTER:  ", end="")
ll1.swap_pairs()
ll1.print_list()
print("-----------------------------------")

# Test case 2: Swapping pairs in a list with an odd number of nodes (1->2->3->4->5)
print("\nTest case 2: Swapping pairs in a list with an odd number of nodes.")
ll2 = LinkedList(1)
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(5)
ll2.append(6)
ll2.append(7)
print("BEFORE: ", end="")
ll2.print_list()
print("AFTER:  ", end="")
ll2.swap_pairs()
ll2.print_list()
print("-----------------------------------")

# Test case 3: Swapping pairs in a list with a single node (1)
print("\nTest case 3: Swapping pairs in a list with a single node.")
ll3 = LinkedList(1)
print("BEFORE: ", end="")
ll3.print_list()
print("AFTER:  ", end="")
ll3.swap_pairs()
ll3.print_list()
print("-----------------------------------")

# Test case 4: Swapping pairs in an empty list
print("\nTest case 4: Swapping pairs in an empty list.")
ll4 = LinkedList(1)
ll4.make_empty()
print("BEFORE: ", end="")
ll4.print_list()
print("AFTER:  ", end="")
ll4.swap_pairs()
ll4.print_list()
print("-----------------------------------")

# Test case 5: Swapping pairs in a list with two nodes (1->2)
print("\nTest case 5: Swapping pairs in a list with two nodes.")
ll5 = LinkedList(1)
ll5.append(2)
print("BEFORE: ", end="")
ll5.print_list()
print("AFTER:  ", end="")
ll5.swap_pairs()
ll5.print_list()
print("-----------------------------------")
