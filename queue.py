''' fifo
queue 1->2->3->4->/
1. none terminated end is at the top (last in)
    adding 4 is O(1)- no need to modify other nodes, if we maintain reference to the tail node of linked list
    removing 4 is O(n)- we need to traverse the ll and change next of 3 to none.

    adding 1 is O(1)- no need to modify other nodes
    removing 1 is O(1)- no need to modify other nodes

    we need to add nodes so that the current tail points to the new node.the new node is none terminated -O(1)
    we need to remove nodes from the head, O(1)

    last in has the none terminated end
'''

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1

    def print_queue(self):
        temp=self.first
        while temp:
            print("<-",temp.value, end=" ")
            temp=temp.next

    def enqueue(self,value):
        new_node=Node(value)
        if self.length==0:
            self.first=new_node
            self.last=new_node
            self.length=1
        else:
            self.last.next=new_node
            self.length+=1
            self.last=new_node

    def dequeue(self):
        if self.length==0:
            return None
        else:
            temp=self.first
            self.first=temp.next
            self.length-=1
            return temp.value


q1=Queue(5)
q1.enqueue(6)
q1.enqueue(7)
q1.enqueue(8)
q1.enqueue(9)
q1.print_queue()
print("\n","-"*20)
val=q1.dequeue()
print(val)
q1.print_queue()