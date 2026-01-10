class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        res = [0] * (n - k + 1)
        

        for i in range(n-k+1):
            state = 0
            for j in range(i+1, i+k):
                if (nums[j] - nums[j-1])!= 1:
                    state = -1
                    break
                    
                
            res[i] = -1 if state==-1 else nums[i+k-1]

        return res
            