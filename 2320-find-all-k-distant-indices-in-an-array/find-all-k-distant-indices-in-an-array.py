class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        n = len(nums)
        j = 0
        ans = []
        seen = set()
        for i in range(n):
            if nums[i]==key:
                # print(i-k, i, min(i+k,n))
                for j in range(max(0,i-k), min(i+k+1, n)):
                    if j not in seen:
                        ans.append(j)
                        seen.add(j)
        return ans