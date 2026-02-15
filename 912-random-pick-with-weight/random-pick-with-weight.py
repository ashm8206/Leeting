class Solution:

    def __init__(self, w: List[int]):
        #res =[1,3,3,3] 
        # since denom is same: We can ignore it

        # We take prefix_sum, cuz it gives us CDF, Cummulative ranges
        
        '''Compute the prefix sum:
        Given the array w = [1, 3, 2]:


        prefix_sum = [1,     4, 6]
        This means:  [[0,1), [1,4), [4,6)]

        Here's how it works:

        If the random target is between 0 and 1, we pick index 0.
        If the random target is between 1 and 4, we pick index 1.
        If the random target is between 4 and 6, we pick index 2
        '''

        self.n = len(w)
        self.prefix_sum = [0] * (self.n + 1)
        

        for i in range(self.n):
            self.prefix_sum[i+1] = self.prefix_sum[i] + w[i]

        
        self.total = self.prefix_sum[-1]

        # https://leetcode.com/problems/random-pick-with-weight/solutions/671921/python-3-simple-solution


    def pickIndex(self) -> int:
        # target = random.randint(0, self.total-1)
        # Generate a number between 0 .. W[n-1]

        target = self.total * random.random()
        # what index is is found for this number? give the leftmost
        
        l = 0
        r =  len(self.prefix_sum) 
        while (l < r):
            m = (l + r) // 2
            if self.prefix_sum[m] < target:
                l = m + 1
            else:
                r = m
        return l - 1 if l > 0 else l
        # return l - 1
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()