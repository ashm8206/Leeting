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
        # arr = []
        output = 0
        for num in range(1,n+1):
            if num not in banned:
                curr_sum+=num
                output+=1
            if curr_sum > maxSum:
                curr_sum-=num
                output-=1
                break
        return output

        