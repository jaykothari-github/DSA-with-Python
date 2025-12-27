class Node:
    def __init__(self,value):

        self.value = value
        self.next = None
        self.prev = None            # For DLL


class DoublyLinkedList:

    def __init__(self,value):

        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1
        return
    
    def print_dll(self):
        
        run = self.head
        while run:
            print(f" {run.value} >" ,end="")
            run = run.next
        print("", run)

    def append(self, value):
        new_node = Node(value)          # Creating new DLL node

        if self.head is None:           # checking head is none or not
            self.head = new_node        # if none than set head and tail to new node
        else:
            self.tail.next = new_node   # if not then changing tail's next to new node
            new_node.prev = self.tail   # attaching new node's prev to tail point
        self.tail = new_node            # changing tail point
        self.length += 1

        return True

    def pop(self):

        if self.head is None:           # for empty DLL
            return None
        elif self.head.next is None:    # For single node DLL
            temp = self.head
            self.head = None            # removing head and tail
            self.tail = None
            self.length -= 1            # decreasing length

            return temp                 # returning node
        
        temp = self.tail                # setting a var at tail
        self.tail = self.tail.prev      # changing tail to prev's node
        self.tail.next = None           # changing current tail's next to none
        temp.prev = None                # detaching last node's prev
        self.length -= 1

        return temp                     # returning var
    

    def prepend(self,value):
        new_node = Node(value)          # Creating new node

        if self.head is None:           # if DLL is empty then setting head and tail to new node
            self.head = new_node
            self.tail = new_node
        else:                           # if not then 
            self.head.prev = new_node   # changing head's prev to new node
            new_node.next = self.head   # changing new node's next to head
            self.head = self.head.prev  # changing head point
        self.length += 1

        return True
    

    def pop_first(self):
        var = self.head                 # setting a var at head
        if self.head is None:           # For Empty DLL
            return None
        if self.head.next is None:      # for single node DLL
            self.head = None
            self.tail = None
            self.length -= 1
            return var
        self.head = self.head.next      # changing head to head's next
        var.next = None                 # setting var's next to None
        self.head.prev = None           # changing current head's prev to None
        self.length -= 1

        return var
    
    def get(self,index):

        if index < 0 or index >= self.length:           # For empty DLL
            return None
        
        if index < self.length / 2:                     # if the index is in first half
            var = self.head                             # starting from Head
            for i in range(index):
                var = var.next
            return var
        else:                                           # if index is in second half
            var = self.tail                             # starting from tail
            for i in range(self.length - index -1):     # length - index move to reach
                var = var.prev
            return var




my_dll = DoublyLinkedList(7)
my_dll.append(8)
my_dll.append(9)
my_dll.append(10)
my_dll.append(11)
my_dll.append(12)
my_dll.append(13)
my_dll.append(14)
my_dll.pop()
my_dll.prepend(10)


my_dll.print_dll()

my_dll.pop_first()

print("----------After------------")

print("Head > ",my_dll.head.value)
print("tail > ",my_dll.tail.value)
print("Length > ",my_dll.length)
my_dll.print_dll()

print(my_dll.get(6).value)
