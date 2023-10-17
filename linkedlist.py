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

    def printLL(self):
        temp=self.head
        while temp is not None:
            print(temp.value, end="-->") #print(temp) prints node object
            temp=temp.next #next is a keyword in python
        print("/")

    def append(self, value):
        #append to end of node
        #special case- LL is empty
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True
#    def pop(self):
#        if self.length !=0:
#           temp=self.head
#            while temp.next!=self.tail:
#                temp=temp.next
#            self.tail=temp
#            temp=temp.next #original tail node
#            self.tail.next=None
#            self.length-=1
#            return temp.value
#        else:
#            return None
        #this code does not work for LL of length 1. as the while loop will fail when we attempt to fetch next value of temp.
        #None type does not have attribute next

    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while(temp.next): #we are only checking truth value
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0: #for ll with 1 node, head and tail will still be pointing at the same node
            self.head=None
            self.tail=None
        return temp #return node object

    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True

    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp

    def get(self,index):# fetch item based on index
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index): #use underscore if there is no use of loop variable inside loop
            temp=temp.next
        return temp

    def set_value(self,index,value): #set is keyword in python
        temp=self.get(index) #could return none
        if temp:
            temp.value=value
            return True
        return False

    def insert(self,index,value):
        #if self.length==0 or index>=self.length:
        #    self.append(value)
        #elif index<0:
        #    self.prepend(value)
        if index<0 or index>self.length:
            return False
        if index==self.length:
            return self.append(value)
        if index==0:
            return self.prepend(value)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True

    def remove(self,index): #return removed node
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        pre=self.get(index-1)
        temp=pre.next
        pre.next=temp.next
        temp.next=None
        self.length-=1
        return temp

    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after



LL1=LinkedList(10)
LL1.append(20)
LL1.append(30)
LL1.append(40)
LL1.append(50)
LL1.append(60)
LL1.printLL()
val=LL1.pop().value
print(val)
LL1.printLL()
val=LL1.get(2).value
print(val)
LL1.printLL()
LL1.set_value(1,100)
LL1.printLL()
LL1.insert(3,89)
LL1.printLL()
LL2=LinkedList(10)
val=LL2.pop().value
LL2.insert(-3,89)
LL2.printLL()
LL1.reverse()
LL1.printLL()