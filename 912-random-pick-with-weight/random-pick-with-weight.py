class Solution:

    def __init__(self, w: List[int]):
        #res =[1,3,3,3] 
        # val =uniform distribution over randint(0,sum(w))
        # return idx of Val in prefix sum

        
        
        self.n = len(w)
        self.prefix_sum = [0]* self.n
        self.prefix_sum[0] = w[0]

        for i in range(1,self.n):
            self.prefix_sum[i] = self.prefix_sum[i-1] + w[i]

        self.total = self.prefix_sum[-1]
  

        # https://leetcode.com/problems/random-pick-with-weight/solutions/671921/python-3-simple-solution


    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        # target = self.total * random.random()
        # idx = bisect.bisect_left(self.prefix_sum, target)

        l = 0
        r =  len(self.prefix_sum)
        while (l < r):
            m = (l + r) // 2
            if self.prefix_sum[m] < target:
                l = m + 1
            else:
                r = m
        return l
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()