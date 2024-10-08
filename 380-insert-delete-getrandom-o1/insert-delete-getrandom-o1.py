from random import choice, choices
class RandomizedSet():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        # We want to do random sampling.
        # We are maintaining a list for the "choice" / "choices" func
        #  These two functions only use (List, Tuple, and range values)

        # Since we are maintaing a list, we will, have to keep it insync with the hashmap insert and remove O(1) time.
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
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # Returns a value from self.list with replacement
        return choice(self.list)

        # Below returns a list, integer is expected
        # return choices(self.list, weights=[1]*len(self.list), k = 1)[0]