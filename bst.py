'''full tree- all nodes point to either 2 or 0 nodes
perfect tree- any level of the tree that has nodes is completely filled in that level
complete tree- nodes are filled in a level from left to right without gaps
parent node, child node, a node can have only one parent
leaf node- no children
root node- no parent'''

'''binary search tree
for a node, the left branch holds values less than it, right hold nodes greater than it
num of nodes=(2^n)-1, n is number of levels
to find a node, max of n steps to find it - to add and remove - O(logn)

O(logn) achieved by divide and conquer, very efficient

worst case- tree never forks - resembles linked list- O(n)'''

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None #create empty tree

    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        else:
            temp=self.root
            while True:
                if new_node.value==temp.value: #if you compare nodes it will be unique. check for value
                    return False #bst cannot have duplicates
                if new_node.value<temp.value:
                    if temp.left is None:
                        temp.left=new_node
                        return True 
                    temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=new_node
                        return True
                    temp=temp.right

    def contains(self,value): #binary search
        if not(self.root):
            return False
        temp=self.root
        while temp:
            if value==temp.value: #check if current temp is equal to value, return true if found
                return True
            if value<temp.value: #if value not found, compare and move to correct branch
                 temp=temp.left
            else:
                temp=temp.right
            #repeat loop until temp is None- no match founf
        return False #loop exited, no match found

    '''recursive case and base case
    condition must eventually lead to the base case otherwise it will cause stack overflow
    each instance of function call is added to the call stack and the most recent call is processed first
    '''
    #recursive contains function
    def __r_contains(self,current_node,value):
        if current_node==None: #no matching node, return false
            return False 
        if value==current_node.value: #node found, return true
            return True
        if value< current_node.value: #value is less than the current node, we need to traverse to the left of the current node, call the function recursively and give current node as the left node
            return self.__r_contains(current_node.left,value)
        if value> current_node.value: #similar to less than, traverse the right branch of current node if the value is greater than
            return self.__r_contains(current_node.right,value)
    

    def r_contains(self,value): #main function to call the recursive function above
        return self.__r_contains(self.root,value)


    def __r_insert(self,current_node, value):
        if current_node==None:
            return Node(value) #node to be inserted at correct empty spot found
        if value < current_node.value:
            current_node.left=self.__r_insert(current_node.left ,value)
        if value > current_node.value:
            current_node.right=self.__r_insert(current_node.right ,value)
        return current_node #pointer to existing node
        #the fucntion takes care of duplicate nodes as we do not have a equal to case,the current_node is returned and the parent node continues to point at current node,  no new node is adde


    def r_insert(self,value):
        if self.root==None:
            self.root=Node(value) 
        self.__r_insert(self.root,value) 

    def min_value(self,current_node):  #returns the minimum value in a subtree/ tree
        while (current_node.left is not None):
            current_node=current_node.left
        return current_node.value #return value not node

    def __delete(self,current_node,value):
        if current_node==None : #value is not in the tree
            return None

        #traverse the tree to find the node with given value        
        if value < current_node.value:
            current_node.left=self.__delete(current_node.left ,value)
        
        elif value > current_node.value:
            current_node.right=self.__delete(current_node.right ,value)
        
        else: #value is found, equal to case
            #4 cases- leaf node, has left child only, has right child only, has both left and right child
            if current_node.left==None and current_node.right==None: #leaf node
                return None #make the parent node point to none
            
            elif current_node.left==None: #node to be removed has right child
                current_node=current_node.right #effectively making the parent node point to the right child of the node to be removed
            
            #similarly for just left child
            elif current_node.right==None:
                current_node=current_node.left
            
            else: #has both children, we need to replace the node to be removed with min value on the right subtree, to maintain a valid bst
                sub_tree_min=self.min_value(current_node.right)
                current_node.value=sub_tree_min #replace current node
                current_node.right=self.__delete(current_node.right ,sub_tree_min) #similar to deleting leaf node, but here we pass min value of subtree
        return current_node



    def delete(self,value):
        self.__delete(self.root,value)

    #find min and max
    #find successor and predecessor

    '''     5
       3         7
    2     4    6     8
    Bfs of this tree should give [5,3,7,2,4,6,8] level wise
    inorder [2,3,4,5,6,7,8] left root right 
    postorder [2,4,3,6,8,7,5] left right root
    preorder [5,3,2,4,7,6,8] root left right
    '''  

    #all nodes present in the same level are traversed completely before traversing the next level, left to right
    def BFS(self):
        current_node=self.root
        queue=[] #holds nodes that we see
        results=[]
        queue.append(current_node)
        while len(queue)>0:
            current_node=queue.pop(0)
            results.append(current_node.value) #pop the first node in queue and append to results
            if current_node.left is not None: #if current node has left child append it to queue
                queue.append(current_node.left)
            if current_node.right is not None: #similarly right child
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        results=[]
        def traverse(current_node): #helper function, recursive approach
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    def dfs_post_order(self):
        results=[]
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    #check if bst is valid or not, inorder gives values in ascending order
    def is_valid_bst(self):
        values=self.dfs_in_order()
        for i in range(1,len(values)):
            if values[i-1]>=values[i]:
                return False
        return True

    def kth_smallest(self,k):
        self.kth_count=0
        return self.kth_smallest_node(self.root,k)

    #basically performs inorder traversal
    #traverse the entire left subtree, find smallest element, return it and increment kth, if equal to k return it, 
    #otherwise recursively traverse right subtree
    def kth_smallest_node(self,node,k): 
        if node is None:
            return None
        left_result=self.kth_smallest_node(node.left,k)
        if left_result is not None:
            return left_result
        self.kth_count+=1
        if self.kth_count==k:
            return node.value
        right_result=self.kth_smallest_node(node.right,k)
        if right_result is not None:
            return right_result
        return None

bst1=BST()
bst1.insert(44)
bst1.insert(12)
bst1.insert(67)
bst1.insert(4)
bst1.insert(59)
bst1.insert(39)
print(bst1.dfs_in_order())
print()
print("39 present in bst1 ",bst1.contains(39))
print("8 present in bst1 ", bst1.contains(8))
print()
bst1.delete(39)
print("Deleted node: 39\n",bst1.dfs_in_order())
print()

print("Recursive")
bst2=BST()
bst2.r_insert(2)
bst2.r_insert(14)
bst2.r_insert(6)
bst2.r_insert(9)
bst2.r_insert(7)
print(bst2.dfs_in_order())
print()
print("6 present in bst2 ", bst2.contains(6))
print("14 present in bst2 ",bst2.contains(14))
print(bst2.dfs_in_order())
print()
print("4th smallest node: ", bst2.kth_smallest(4))
bst2.delete(9)
print("Deleted node: 9\n",bst2.dfs_in_order())


print()
bst3=BST()
'''insertion in ascending or descending order of values leads to a linear structure, not a balanced tree. insert in random order
bst3.insert(2)
bst3.insert(3)
bst3.insert(4)
bst3.insert(5)
bst3.insert(6)
bst3.insert(7)
bst3.insert(8)
this will cause tree to look like:
     2
      \
       3
        \
         4
          \
           5
            \
             6
              \
               7
                \
                 8
'''
bst3.insert(5)
bst3.insert(7)
bst3.insert(3)
bst3.insert(6)
bst3.insert(4)
bst3.insert(2)
bst3.insert(8)
'''      5
       /   \
      3     7
     / \   / \
    2   4 6   8
'''
print("Traversals")
print("BFS")
print(bst3.BFS())
print("Preorder")
print(bst3.dfs_pre_order())
print("Postorder")
print(bst3.dfs_post_order())
print("Inorder")
print(bst3.dfs_in_order())