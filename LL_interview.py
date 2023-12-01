#floyd's cycle finding algorithm
#hare- tortise algo, fast and slow pointer
#can also be used to find middle node without using length
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self, value): #define head, tail and length
        new_node= Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def printLL(self):
        temp=self.head
        while temp is not None:
            print(temp.value, end="-->") #print(temp) prints node object
            temp=temp.next #next is a keyword in python
        print("/")

#if fast reaches end of the list or has no next node, slow pointer will be at the middle of the list
#for list with even length, function returns 1st value of 2nd half of list
    def find_middle_node(self):
        slow=self.head
        fast=self.head
        while fast!= None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow

#same approach, but loop detected when slow and fast are at the same pointer
    def has_loop(self):
        fast=self.head
        slow=self.head
        while fast!=None and fast!=self.tail:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        else:
            return False

#split list based on input x, first half being values less than x, second half greater than x
#2 strings maintained then merged in the end
#need to update tail- more complex
    def partition_list(self,x):
        if self.head is None:
            return None
        dummy1=Node(0)
        dummy2=Node(0)
        prev1=dummy1
        prev2=dummy2
        current=self.head
        while current is not None:
            if current.value<x:
                prev1.next=current
                prev1=current
            else:
                prev2.next=current
                prev2=current
            current=current.next
        prev1.next=None
        prev2.next=None
        prev1.next=dummy2.next
        self.head=dummy1.next

    #have 2 pointers and 2 loops, compare and remove
    #more efficient to use set
    def remove_duplicates(self):
        current=self.head
        while current:
            runner=current
            while runner.next:
                if runner.next.value==current.value:
                    runner.next=runner.next.next
                    self.length-=1
                runner=runner.next
            current=current.next

    #same function with set
    #a set cannot have duplicate values. and its values cannot be changed (can add and remove tho)
    def remove_duplicates_set(self):
        values = set()
        previous = None #last unique node
        current = self.head
        while current:
            if current.value in values: #duplicate node
                previous.next = current.next
                self.length -= 1
            else: #unique node
                values.add(current.value)
                previous = current
            current = current.next

    #reverse nodes bwtween 2 indices
    #similar to list reversal, but here we need to reverse only end-start number of nodes
    def reverse_between(self, start,end):
        if self.length<=1:
            return
        dummy=Node(0) #sentinel or placeholder node, handles edge cases
        #This eliminates the need for special cases when the reversal starts from the head
        dummy.next=self.head
        prev=dummy
        for _ in range(start):
            prev=prev.next
        current=prev.next
        for _ in range(end-start):
            node_move=current.next
            current.next=node_move.next
            node_move.next=prev.next
            prev.next=node_move
        self.head=dummy.next
    

#independent function written, not inside ll class
#to find kth node from end without using length, create node fast and slow
#create a gap of k nodes btw fast and slow using for loop
#then loop until fast reaches the element after tail- none
#return slow
#If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.
def find_kth_from_end(ll,k):
    slow=ll.head
    fast=ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast=fast.next 
    while fast:
        slow=slow.next
        fast=fast.next
    return slow


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
my_linked_list_2.append(5)
print(my_linked_list_2.has_loop() )
my_linked_list_2.printLL()
print(find_kth_from_end(my_linked_list_2, 2).value)