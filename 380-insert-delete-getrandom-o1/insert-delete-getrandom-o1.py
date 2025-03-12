from random import choice
class RandomizedSet():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict:
            return False

        # move the last element to the place idx of the element to delete
        last_element, idx = self.list[-1], self.dict[val]
        self.list[idx] = last_element
        self.dict[last_element] = idx

        # delete the last element. from list
        self.list.pop()
        # delete val from dict
        del self.dict[val]
        return True
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)

# import random
# class RandomizedSet():

#     def __init__(self):
#         self.nums, self.pos = [], {}
        
#     def insert(self, val):
#         if val not in self.pos:
#             self.nums.append(val)
#             self.pos[val] = len(self.nums) - 1
#             return True
#         return False
        

#     def remove(self, val):
#         if val in self.pos:
#             idx, last = self.pos[val], self.nums[-1]
#             #idx of val and  the last element in list

#             self.nums[idx], self.pos[last] = last, idx
#             # place last, where removing element used to be
#             # pos[last] = idx

#             # we over-wrote this number

#             self.nums.pop(); self.pos.pop(val, 0)
#             # evict last element,
#             # remove from dict self.pos.pop(val,0)
#             return True
#         return False

#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         # Returns a value from self.list with replacement

#         # return random.choice(self.nums) 
#         # ^^ Returns one element with equal probablity
#         return self.nums[random.randint(0, len(self.nums)-1)]
#         # ^^ return idex, you need to get the number

