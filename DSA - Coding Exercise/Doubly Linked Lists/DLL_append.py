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


my_dll = DoublyLinkedList(7)
my_dll.append(8)
print("Head > ",my_dll.head.value)
print("tail > ",my_dll.tail.value)
print("Length > ",my_dll.length)

my_dll.print_dll()


