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
    
    def append(self,value): #add value at the end
        new_node=Node(value)
        if self.length==0:
            self.tail=new_node
            self.head=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def pop(self): #do not forget to update tail
        if self.length==0:
            return None
        if self.length==1:
            temp=self.head
            self.head=None
            self.tail=None
        else:
            temp=self.tail
            temp2=temp.prev
            temp.prev=None
            temp2.next=None
            self.tail=temp2
        self.length-=1
        return temp

    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.tail=new_node
            self.head=new_node
        else:
            temp=self.head
            temp.prev=new_node
            new_node.next=temp
            self.head=new_node
        self.length+=1

    def pop_first(self):
        if self.length==0:
            return None
        if self.length==1:
            temp=self.head
            self.head=None
            self.tail=None
        else:
            temp=self.head
            temp2=temp.next
            temp.next=None
            temp2.prev=None
            self.head=temp2
        self.length-=1
        return temp

    #similar to linked list, but more efficient if we split the dll and pick if we have to traverse from tail or head depending on index
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        if index <self.length//2:
            temp=self.head
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp
    
    def set_value(self,index,value):
        if index<0 or index>=self.length:
            return False
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
#for insert and remove use pop prepend append and popo first
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        new_node=Node(value)
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        before=self.get(index-1)
        after=before.next
        new_node.prev=before
        new_node.next=after
        before.next=new_node
        after.prev=new_node
        self.length+=1
        return True

    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        temp=self.get(index)
        temp.next.prev=temp.prev
        temp.prev.next=temp.next
        temp.prev=None
        temp.next=None
        self.length-=1
        return temp
    

Dll=DoubleLinkedList(10)
Dll.printDLL()
val=Dll.pop().value
Dll.printDLL()
Dll.append(20)
Dll.append(30)
Dll.append(40)
Dll.append(50)
Dll.append(60)
Dll.append(70)
Dll.append(80)
Dll.printDLL()
val=Dll.pop().value
print(val)
Dll.printDLL()
Dll.prepend(100)
Dll.printDLL()
Dll.pop_first()
Dll.printDLL()
print(Dll.get(4).value)
Dll.set_value(2,100)
Dll.printDLL()
Dll.insert(3,200)
Dll.printDLL()
print(Dll.remove(3).value)
Dll.printDLL()