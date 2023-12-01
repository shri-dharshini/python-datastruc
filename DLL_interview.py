class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def printDLL(self):
        temp=self.head
        while temp is not None:
            print(temp.value, end="-->") #print(temp) prints node object
            temp=temp.next #next is a keyword in python
        print("/")

    def swap_first_last(self):
        if self.length<=1:
            return False
        tail_value=self.tail.value
        self.tail.value=self.head.value
        self.head.value=tail_value
        return True

    def reverse(self):
        if not(self.head):
            return
        temp=self.head
        while temp:
            after=temp.next #store next node
            temp.next=temp.prev #assign next node as prev node
            temp.prev=after #assign prev node as the stored next node, effectively reversing links for the current node
            temp=after #go to the next node for iteration
        self.tail,self.head=self.head,self.tail

    #from the tail end we have to go to previous
    def is_palindrome(self):
        if self.length<=1:
            return True
        temp1=self.head
        temp2=self.tail
        for _ in range(self.length//2):
            if temp1.value==temp2.value: #compare first and last values as we move closer to the middle
                temp1=temp1.next
                temp2=temp2.prev
            else:
                return False
        return True
    

    #swap pairs of nodes, 1<->2<->3<->4<->5<->6 becomes 2<->1<->4<->3<->6<->5
    def swap_pairs(self):
        dummy=Node(0)#sentinel or placeholder node, handles edge cases
        #This eliminates the need for special cases when the reversal starts from the head
        dummy.next=self.head
        prev_node=dummy
        while self.head and self.head.next:
            first_node=self.head #take 2 nodes at a time
            second_node=self.head.next
            prev_node.next=second_node 
            first_node.next=second_node.next #reverses link in single direction
            second_node.next=first_node
            second_node.prev=prev_node 
            first_node.prev=second_node #reverses link completely
            if first_node.next:
                first_node.next.prev=first_node #Ensure that the node after our swapped pair has its prev updated
            self.head=first_node.next
            prev_node=first_node
        self.head=dummy.next #reassign head
        if self.head:
            self.head.prev=None
