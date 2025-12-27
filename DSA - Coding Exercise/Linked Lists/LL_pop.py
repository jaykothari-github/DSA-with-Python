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

    def append(self, value):
        new_node = Node(value)

        if self.head == None:       # If head is None then it creates a head point
            self.head = new_node
        else:                       # If not then it will just change tail section
            self.tail.next = new_node       # Adding new node to tail

        self.tail = new_node            # after adding node changing the tail point
        self.length += 1                # increasing the length
        
    def pop(self):

        ################# Udemy solution 
        '''
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
        '''
        
        if self.head is None and self.tail is None:
            return None  
        
        elif self.length == 1:
            self.length -= 1
            temp = self.head
            self.head = None
            self.tail = None
            return temp
        
        else:
            temp = self.head
            for i in range(1,self.length):
                if self.length - 1 == i:
                    # print(" last parent node >> ",temp.value)
                    self.tail = temp
                    temp = self.tail.next
                    self.tail.next = None
                    self.length -= 1
                    break

                temp = temp.next
            return temp

    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            



my_linked_list = LinkedList(4)   # Create a new linked list with an initial value of 4

# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)

my_linked_list.append(11)
my_linked_list.append(23)
my_linked_list.append(20)

# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)
# # my_linked_list.print_ll()

print(my_linked_list.pop().value)
my_linked_list.print_ll()

print("###############################")
my_linked_list.print_ll()


print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)