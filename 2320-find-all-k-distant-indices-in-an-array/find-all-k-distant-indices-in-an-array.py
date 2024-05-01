class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        n = len(nums)
        j = 0
        ans = []
        for i in range(n):
            if nums[i]==key:
                for j in range(max(j,i-k), min(i+k+1, n)):
                    if j not in ans:
                        ans.append(j)
            # 0,1,2
    
        return ans
