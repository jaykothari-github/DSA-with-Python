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

        ################# Udemy solution #################
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
        # ###################################################

        if self.head is None and self.tail is None:   # If head and tail are None
            return None  
        
        elif self.length == 1:                         # If lenght is 1
            self.length -= 1                           # Reducing lenght for pop
            temp = self.head                           # For returning value
            self.head = None                           # Setting Head and tail None
            self.tail = None
            return temp
        
        else:                                           # If Length is > 1
            temp = self.head
            for i in range(1,self.length):              # Running loop to get last parent node
                if self.length - 1 == i:                # if current iteration is total length -1
                    # print(" last parent node >> ",temp.value)
                    self.tail = temp                    # Setting tail to last parent
                    temp = self.tail.next               # For return
                    self.tail.next = None               # setting tail to None so last child get release
                    self.length -= 1
                    break

                temp = temp.next                        # getting into next node
            return temp


    def prepend(self,value):
        new_node = Node(value)                          # Creating new node for new data
        if self.head is None and self.tail is None and self.length == 0:  # for Empty LL
            self.head = new_node
            self.tail = new_node
        else:                                           # For Non-Empty LL
            new_node.next = self.head                   # attaching new node's next to original Head
            self.head = new_node                        # Changing Head
        self.length += 1                                # Increasing Length
        return True

    def pop_first(self):

        if self.head is None and self.tail is None and self.length == 0:  # For empty LL
            return None
        
        temp = self.head                    # to return
        if self.length == 1:                # if only one element in LL
            self.head = None
            self.tail = None
        else:                               # if more than 1 element 
            self.head = self.head.next      # changing original head to child's head
        self.length -= 1                    # decreasing length
        temp.next = None                    # detaching pop value from LL pointer
        return temp
    
    def get(self,index):
        if index < self.length and index >= 0:      # checking the range on val and LL index
            temp = self.head                        # For return or iteration
            for i in range(index):                  # iterating no of index times value
                temp = temp.next                    # Going to next node
            
            return temp                             # EOL returning temp
        else:
            raise IndexError("Index Out of range")  # If val is out of index then raise exp or return None
            # return None
        
            
    def set_value(self,index,value):
        # temp = self.head                        # For iteration
        # if index < self.length and index >= 0:  # checking index is valid or not
        #     for i in range(index):              # going to index
        #         temp = temp.next                # Changing node to next
        #     else:
        #         temp.value = value              # After completion loop it change the value of that index
        #     return True
        # else:
        #     return None                         # If index is not valid then return None
       
        temp = self.get(index)              # Using get method to get the node
        if temp:                            # if it is not none
            temp.value = value              # changing the value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:    # For out of index
            return False
        
        elif index == 0:                        # Prepand- adding at index 0
            return self.prepend(value)
            
        #######################################################
        temp = self.head                        # any other index
        for i in range(index):                  # going to index
            pre = temp                          # setting neighbor indexes
            temp = temp.next
        else:                                   # after completing loop
            new_node = Node(value)              # creating node
            new_node.next = temp                # setting next
            pre.next = new_node                 # setting pre

        self.length += 1
        return True
        ###################  OR  #############################
        ##### Udemy ##### 

        # if index == self.length:              # if inserting on last index >> calling append
        #     return self.append(value)
        # new_node = Node(value)
        # temp = self.get(index - 1)            # get n - 1 index 
        # new_node.next = temp.next             # setting new node's next to current node's next
        # temp.next = new_node                  # now changing current node's next
        # self.length += 1   
        # return True  
    
        #########################################################

    def remove(self,index):
        if index < 0 or index >= self.length:   # Out of index
            return 
        if index == 0:                          # if remove from 0
            return self.pop_first()
        elif index == self.length - 1:          # if remove from last
            return self.pop()
        pre = self.get(index - 1)               # getting pre point of remove val
        cur = pre.next                          # point of remove
        pre.next = cur.next                     # pre point redirected to next of current
        cur.next = None                         # current point detached and set to None
        self.length -= 1
        return cur

    def reverse(self):
        temp = self.head                            # Creating current point
        before = None                               # Creating pre point

        for i in range(self.length):
            after = temp.next                       # pointing to next point
            temp.next = before                      # current's next point target to pre point
            before = temp                           # pre point change to current
            temp = after                            # current change to next node

        self.head, self.tail = self.tail, self.head # After reversing swapping head and tail

    def print_ll(self):
        temp = self.head                # Setting a temp var
        while temp is not None:         # Looping with temp var until temp become None
            print(temp.value)
            temp = temp.next            # getting into child node with next
            



my_linked_list = LinkedList(4)   # Create a new linked list with an initial value of 4

my_linked_list.append(11)
my_linked_list.append(23)
my_linked_list.append(20)

# my_linked_list.print_ll()

my_linked_list.set_value(0,222)

# my_linked_list.print_ll()


# print("#############  Insert  ###########")

my_linked_list.insert(0,100)
my_linked_list.print_ll()

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

print("############## Remove #################")

print("Printing pop value >>>>  ",my_linked_list.remove(1).value)
my_linked_list.print_ll()

# my_linked_list.reverse()
# my_linked_list.print_ll()

# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)
