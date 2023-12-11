#Sets can only contain unique elements (meaning that duplicates are not allowed)
#enables faster lookup (O(1))
def remove_duplicates(my_list):
    set1=set(my_list)
    return list(set1)


def has_unique_chars(string):
    string=''.join(sorted(string)) #sort the string
    set1=sorted(set(string)) #eliminate duplicates
    if ''.join(set1)==string: #check if str formed by set and original str are eq
        return True
    return False


#find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.
def find_pairs(arr1,arr2,target):
    pairs=[]
    set1=set(arr1) #faster lookup, unique pairs as we use set()in only one array
    for i in arr2:
        compl=target-i
        if compl in set1:
            pairs.append((compl,i))
    return pairs

#length of sequence of integers in which each element is one greater than the previous element
def longest_consecutive_sequence(nums):
    num_set=set(nums) #unique elements only, faster lookup
    longest_seq=0 #hold length
    for num in nums:
        if num-1 not in num_set: #see if value less than current num exists in set
            current_num=num 
            current_seq=1
            while current_num+1 in num_set: #count up seq num as long as there exists a consecutive sequence number
                current_num+=1
                current_seq+=1
            longest_seq=max(longest_seq,current_seq) #update longest seq is current seq is greater
    return longest_seq


print(remove_duplicates([1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]))
print("-"*50)

print(has_unique_chars('0123456789')) #True
print(has_unique_chars('abacadaeaf')) #False
print("-"*50)

print(find_pairs([1, 2, 2, 3], [3, 3, 4, 4], 6))
print("-"*50)

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) ) #output-4 as longest conseq seq is[4,3,2,1]