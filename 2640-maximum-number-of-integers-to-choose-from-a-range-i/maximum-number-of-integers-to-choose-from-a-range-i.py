class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """

        banned = set(banned)
        curr_sum = 0
        arr = []
        for i in range(1,n+1):
            if i not in banned:
                curr_sum+=i
                arr.append(i)
            if curr_sum > maxSum:
                curr_sum-=arr.pop()
                return len(arr)
        return len(arr)

        