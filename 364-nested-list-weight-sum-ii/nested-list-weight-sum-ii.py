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
from collections import deque
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        depth = 1
        maxDepth = 0
        sumofInt = 0
        sumofProd = 0

        '''
        summation: Int*(maxDepth - depth + 1)
        = int * Maxdepth - int*depth + int
        = Summation of Integer 
        = summation Integer * product

        '''
        q = deque(nestedList)

        while q:
            size = len(q)
            maxDepth = max(maxDepth,depth)

            for i in range(size):
                nextInt = q.popleft()
                if nextInt.isInteger():
                    sumofInt += nextInt.getInteger()
                    sumofProd += (nextInt.getInteger() * depth)
                else:
                    q.extend(nextInt.getList())
            if q:
                depth +=1 
        return (maxDepth + 1)*sumofInt - sumofProd
