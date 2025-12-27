class Node:
    def __init__(self,value):

        self.value = value
        self.next = None
        self.prev = None


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
            print(" > ",run.value)
            run = run.next


my_dll = DoublyLinkedList(7)
print("Head > ",my_dll.head.value, my_dll.head.next, my_dll.head.prev)
print("tail > ",my_dll.tail.value)
print("Length > ",my_dll.length)

my_dll.print_dll()


