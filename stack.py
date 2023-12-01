'''filo- first in is 1. last in is 4.
stack 1->2->3->4->/
1. none terminated end is at the top (last in)
    adding 4 is O(1)- no need to modify other nodes. 
    removing 4 is O(n)- we need to traverse the ll and change next of 3 to none.

stack /<-1<-2<-3<-4
2. none terminated end is at the top (first in)
    adding 4 is O(1)- no need to modify other nodes.
    removing 4 is O(1)- no need to modify other nodes.

so we need to implement stack using linked list so that the none terminated node is the
bottom most node ie the first in node. the other nodes must point to the node they are stacking on top of.
'''

class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
    
    def print_stack(self):
        temp=self.top
        while temp:
            print(temp.value)
            temp=temp.next

    def push(self,value):
        new_node=Node(value)
        if self.height==0: #always think of edge cases!!!!
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1

    def pop_stack(self):
        if self.height==0:
            return None
        else:
            temp=self.top
            self.top=self.top.next
            self.height-=1
            return temp.value

s1=Stack(3)
s1.push(4)
s1.push(5)
s1.print_stack()
print("-"*20)
val=s1.pop_stack()
s1.print_stack()
