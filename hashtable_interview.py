#to find if a common item exists in 2 lists
#naive approach- run nested for loops- O(n^2)
#for more efficient approach use dictionary/hash table -> O(n), loop one list, store in ht, loop next list to see if value in ht
def item_in_common(list1,list2):
    check={}
    for i in list1:
        check[i]=True #traverse though first list, assign key(index value) to value True for all nums in list1
        #print(check)
    for j in list2:
        if j in check: #see if any of the items in list2 exist in dict, return True if found
            return True
    return False


def find_duplicates(nums):
    num_counts = {} #create ht
    for num in nums: 
        num_counts[num] = num_counts.get(num, 0) + 1
        #The get() method returns the value of the item with the specified key, 2nd argument is default value, to return when key not found
        #so here the value for each key is the count of the key in nums

    duplicates = [num for num, count in num_counts.items() if count > 1]
    #items() gives each key-value pair as a tuple within a list
    #duplicates thus holds values which have count greater than 1
    return duplicates


def first_non_repeating_char(string):
    check={}
    for i in string:
        check[i]=check.get(i,0)+1 #stores the number of times the char appears
    for i in string:
        if check[i]==1: 
            return i #return the first character that has count 1
    return None

#return a list of lists where each sublist holds anagrams(words that contain same letter)
def group_anagrams(strings):
    check={}
    for i in strings:
        letters=''.join(sorted(i)) 
        if letters in check: 
            check[letters].append(i) #if the sorted letters are already in the ht, append the current word to it
        else:
            check[letters]=[i] #create a list for the sorted letters
            
    return list(check.values())


#find the indices of two numbers in the array that add up to the target
def two_sum(nums,target):
    num_map={} #holds key-num and value-index of num
    for index,value in enumerate(nums):
        complement=target-value #the other value that we need to find in nums
        if complement in num_map: #if the complement exists, return the pair
            return [num_map[complement], index]
        num_map[value]=index
    return []


#finds the indices of a contiguous subarray in nums that add up to the target sum
def subarray_sum(nums,target):
    sum_index={0:-1} #key-sum, value- ending index
    #above sum_index is initialized this way to handle case when first value itself is eq to target
    current_sum=0
    for index,value in enumerate(nums):
        current_sum+=value
        if current_sum-target in sum_index: #check if difference exists as key in ht
            #we are looking for an index, at which sum of prev elements is current_sum-target
            #so when we go from that index to the current index, we get target sum
            return [sum_index[current_sum-target]+1,index]
        sum_index[current_sum]=index
        print(sum_index)
    return []    

#test case for subarray_sum
#[13,14,11,3,3,1,5,14,9], target=12
#{0: -1, 13: 0, 27: 1, 38: 2, 41: 3, 44: 4, 45: 5}- status of ht until value 5 is reached in loop
#when we see 5 in the array, current sum=45+5=50
#current_sum-target=50-12= 38
#we have 38 in ht. which is our starting index- 2+1=3 (we do not need the element at 2nd index)
#ending index is current index - 6
#nums[3:6]=[3,3,1,5]--> sum=12
    
list1 = [1,3,5]
list2 = [2,4,5]
print(item_in_common(list1, list2))
print("-"*50)
print ( find_duplicates([1, 1, 2, 2, 3]) )
print("-"*50)
print( first_non_repeating_char('eetcode') )
print("-"*50)
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )
print("-"*50)
print(two_sum([12, 15, 5, 2, 8, 1, 7], 12))  
print("-"*50)
print(subarray_sum([13,14,11,3,3,1,5,14,9],12))
print("-"*50)



