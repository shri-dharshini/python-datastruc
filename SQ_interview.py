class Stack: #stack implementation using list. top is list[-1]
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def is_balanced_parentheses(parentheses): #check if the string of parenthesis is balanced or not
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p) #push the open parenthesis when encountered
        elif p == ')':
            if stack.is_empty() or stack.pop() != '(': #for a close paranthesis check if the stack is empty (there is no matching open parenthesis), or if the top is not a matching open parenthesis- not balanced
                return False
    return stack.is_empty() #after all the iterations if the stack is empty, ie if there are no open parenthesis left, return true, else there are unmatched open parenthesis- return false

def reverse_string(string):
    stack=Stack()
    for i in string:
        stack.push(i) #push onto the stack in same order of string. from the top if we traverse, the string will be reversed
    temp=''
    for i in range(len(string)):
        val=stack.pop()
        temp=temp+val
    string=temp
    return string

def sort_stack(stack): #sort the stack so that the smallest element is the top
    additional_stack = Stack() #additional stack will have largest element on top so that when we pop and push into stack it will be reversed
    while not stack.is_empty(): #repeat until no elements left
        temp = stack.pop() #take top element
        while not additional_stack.is_empty() and additional_stack.peek() > temp: #check if addn stack is not empty and if the top of addn is greater than temp
            stack.push(additional_stack.pop()) #we have greater value in addn stack, which needs to go to bottom of stack. so pop from addn and push to stack
            #repeat until all the elements greater than temp have been pushed into stack in descending order towards top

        additional_stack.push(temp) #push temp when either addn stack is empty or temp is less than top of addn
    #end of while, all elements of stack popped
    while not additional_stack.is_empty(): #push remaining elements of addn into stack
        stack.push(additional_stack.pop())


#queue using stack. stack1 holds the queue, top is first in. 
#to append data we need to pop all elements from stack1, push to stack2 and push the data. Then pop from stack2 and append to stack1.
#top remains same
#removal of data is simply pop.


class MyQueue: 
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if len(self.stack1)==0:
            return None
        return self.stack1.pop()
        
    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0

    def print_queue(self):
        for i in range(len(self.stack1)-1, -1, -1):
            print(self.stack1[i])
        


str1="((()))))"
str2="(())()(())"
str3="(()())("
print(is_balanced_parentheses(str1))
print(is_balanced_parentheses(str2))
print(is_balanced_parentheses(str3))

str1="hello"
print()
print(reverse_string(str1))

s1=Stack()
s1.push(8)
s1.push(10)
s1.push(18)
s1.push(3)
s1.push(6)
s1.print_stack()
print("-"*30)
sort_stack(s1)
s1.print_stack()

print("-"*50)

q1=MyQueue()
q1.enqueue(9)
q1.enqueue(10)
q1.enqueue(4)
q1.print_queue()
q1.dequeue()
q1.print_queue()
