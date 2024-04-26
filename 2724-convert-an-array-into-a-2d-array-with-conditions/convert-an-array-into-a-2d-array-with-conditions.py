from collections import defaultdict
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        

        maps = defaultdict(int)
        
        maxFreq = -1

        for num in nums:
           maps[num]+=1
           maxFreq = max(maxFreq,maps[num])
        
        ans = [[] for _ in range(maxFreq)]

        for num in nums:
            idx = maps.get(num)
            ans[idx-1].append(num)
            maps[num]-=1
        
        return ans

        # 1, 3, 4, 2  ()
        # 1, 3
        # 1

        

