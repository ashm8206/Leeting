from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = defaultdict(set)


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.dict[val].add(len(self.list))
        self.list.append(val)
        return len(self.dict[val]) == 1


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.dict[val]: 
            return False
        last_element, remove_one_idx = self.list[-1], self.dict[val].pop()
        self.list[remove_one_idx] = last_element
        self.dict[last_element].add(remove_one_idx)
        # ?
        self.dict[last_element].discard(len(self.list) - 1)

        self.list.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.list)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()