'''heap is a complete tree, 
max heap- each node holds value greater or equal to its descendents
min heap- each node holds value lesser or equal to its descendents
not good for searching
can be used to quickly remove max or min value
height= logn (n is number of nodes)
can have duplicate values- descendent can be same as parent

implemented using list- leave zero index empty (makes math easier)
left child of a node= 2*parent node index
right child of a node= 2*parent node index+1 (can also implement trees using array like this)

find parent of a node= child node index//2 (integer division)'''

'''Inserting a node
always fill the heap such that it remains a complete tree. then modify the tree by comparing
compare node with its parent, swap if new node is greater, do this operation until the parent node is higher than new node or the new node becomes root
'''

#we are using zero index in code

class MaxHeap:
    def __init__(self):
        self.heap=[]
    #helper functions to return indices of left child, right child, parent
    def left_child(self,index):
        return 2*index+1

    def right_child(self,index):
        return 2*index+2
    
    def parent(self,index):
        return (index-1)//2

    #function to swap two nodes, used in inserting and removing node
    def swap(self,idx1,idx2):
        self.heap[idx1],self.heap[idx2]=self.heap[idx2],self.heap[idx1]

    def sink_down(self,index): #helper function for remove
        max_index=index
        while True:
            left_index=self.left_child(index)
            right_index=self.right_child(index)
            #we need to check if the above indices hold any value or not. otherwise we will get IndexError
            #check if they are less than length of heap

            if left_index<len(self.heap) and self.heap[left_index]> self.heap[max_index]:
                max_index=left_index #see if left child is greater than top, reassign max index
            #similarly for right child
            
            if right_index<len(self.heap) and self.heap[right_index]> self.heap[max_index]:
                max_index=right_index 
            
            #swap the top value with its child that has greater value
            if max_index!=index:
                self.swap(index,max_index)
                index=max_index #keep track of the modified top node

            else: #the node is in the right place, no need to perform any operation
                return 


    def insert(self,value):
        self.heap.append(value) #we need to maintain a complete tree
        #first append, then use while loop to compare and alter the heap to make it a valid max heap
        current=len(self.heap)-1

        #cannot use or. if either condition is true then we will go into loop, which is not what we want
        while self.heap[current]>self.heap[self.parent(current)] and current>0:
            self.swap(current,self.parent(current))
            current=self.parent(current)

    #removing an item- we can only remove the top item (root)- i.e. we can only remove the max item in a max heap
    def remove(self):
        #remove the top item
        #IMPT- we need to always maintain a complete tree. so swap the rightmost element in the last level with the top
        #then we can rearrange like in insert- we have to compare top with its descendents and swap is top is smaller
        if len(self.heap)==0: #empty heap
            return None
        
        if len(self.heap)==1:
            return self.heap.pop() 

        max_value=self.heap[0] #top element
        self.heap[0]=self.heap.pop() #set the top element to be the last element in the list
        self.sink_down(0) #maxindex=0
        return max_value

def find_kth_smallest(nums,k):
    heap1=MaxHeap()
    for i in range(len(nums)):
        heap1.insert(nums[i])
        if len(heap1.heap)>k: #only keep k elements in the heap
            heap1.remove()
    return heap1.remove() #removes the max element- since there are only k elements we will get kth smallest element


#return a list of the same length, where each element in the output list is the maximum number seen so far in the input list.
def stream_max(nums):
    heap1=MaxHeap()
    max_val=[]
    for i in range(len(nums)):
        heap1.insert(nums[i])
        max_val.append(heap1.heap[0]) #maximum value seen so far is the 0th element in heap list. we append that to max_val list
    return max_val

'''priority queue implementation is most efficient with heaps. 
can also use tree, but the tree is not always balanced and may lead to edge cases where insertion and removal becomes O(n)
a heap is always complete hence always balanced
maximum sink down is to the height of the heap which is log n-- very efficient'''

heap1=MaxHeap()
heap1.insert(94)
heap1.insert(72)
heap1.insert(32)
heap1.insert(45)

print(heap1.heap)
print()

heap1.insert(100)
print(heap1.heap)

heap1.remove()
print(heap1.heap)


print(find_kth_smallest([31,21,11,51,61,41],2))

print(stream_max([2,4,2,1,4,5,4,3,6,8,4,3,2]))
heap1.insert(100)
print(heap1.heap)

heap1.remove()
print(heap1.heap)
