''' hash function returns an address for the key-value pair 
hash function- one way, deterministic(returns same address for a given key value pair every time)
inbuilt - dictionary


here we are creating a list of lists. each sublist is a key value pair, inserted at the index(address) given by hash function
if function gives same address for 2 key-value pairs, we store both in that address (collision)

get item(key)- run key thru hash and get address
               if multiple key value pair exists, run loop to find corresponding value

collisions- create a list of the multiple list of key-value pairs, and store this in the address---> SEPARATE CHAINING
            find next empty address and put the new key-value pair there ---> LINEAR PROBING (open addressing)

            we are doing separate chaining. (we can also use linkedlist)

better address scheme- have prime number of addresses- eg 0 to 6 (7 addresses) 
                     - (independence from common factors-decreases the likelihood of patterns that may arise from shared factors, creating a more random distribution of hash values)
                     - having prime number increases randomness of the way key-value pairs are distributed, thereby reducing collisions
'''
 #O(1) to set and get as the distrubution is even

class HashTable:
    def __init__(self,size=7): #default size is 7
        self.data_map=[None]*size

    def __hash(self,key): #O(1)
        my_hash=0
        for letter in key:
            my_hash=(my_hash+ord(letter)*23) %len(self.data_map) #% gives value between 0 and size- index to place pair in
            #use any prime number in place of 23
        return my_hash

    def print_table(self):
        for i, value in enumerate(self.data_map):
            print(i,":",value)
        print("-"*50)

    def set_item(self,key,value):
        pair=[key,value]
        index=self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index]=[] #create an empty list at index as we have not it seen yet
        self.data_map[index].append(pair)
        
    def get_item(self,key):
        index=self.__hash(key)
        if self.data_map[index] is None:
            return None
        for i in self.data_map[index]:
            if i[0]==key:
                return i[1]

    def keys(self): #return a list of all keys
        all_keys=[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in self.data_map[i]:
                    all_keys.append(j[0])
        return all_keys


h1=HashTable()
h1.print_table()
h1.set_item("apple",100)
h1.set_item("lemon",200)
h1.set_item("watermelon",300)
h1.set_item("strawberry",400)
h1.set_item("orange",500)
h1.set_item("mango",600)
h1.set_item("pineapple",700)
h1.print_table()
print(h1.get_item("mango"))
print(h1.get_item("blueberry"))
print(h1.keys())