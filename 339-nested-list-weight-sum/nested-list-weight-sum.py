# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from operator import add
from functools import reduce
from collections import deque
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        # self._integerList =[]

        # def flatten_list(nestedList, level):
        #     for nestInt in nestedList:
        #         if nestInt.isInteger():
        #             self._integerList.append((nestInt.getInteger(),level))
        #         else:
        #             flatten_list(nestInt.getList(),level + 1)

        
        # flatten_list(nestedList,1)
        # #print(self._integerList)
        # res  = sum([reduce(mul, tup) for tup in self._integerList])
        # return res

        ans = 0
        depth = 1
        queue = deque(nestedList)

        while queue: 
            size = len(queue)
            for i in range(size):

                x = queue.popleft()

                if x.isInteger(): ans += depth * x.getInteger()

                else: queue.extend(x.getList())
            if queue:
                depth+=1
        return ans 