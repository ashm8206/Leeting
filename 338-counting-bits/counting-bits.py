class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def numBits(x):
            count = 0
            while x != 0:
                x = x & (x - 1) # zeroing out the least significant set bit
                #kernighans
                count += 1
            return count
            
        ans = [0] * (n + 1)
        for x in range(n + 1):
            ans[x] = numBits(x)
    
        return ans                                