# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):

        def flatten_list(nestedList):
            for nestInt in nestedList:
                if nestInt.isInteger():
                    self._integerList.append(nestInt.getInteger())
                else:
                    flatten_list(nestInt.getList())

        self._integerList =[]
        self._position = 0
        flatten_list(nestedList)
    
    def next(self) -> int:
        val = self._integerList[self._position]
        self._position += 1
        return val
        
    
    def hasNext(self) -> bool:
        return self._position < len(self._integerList)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())