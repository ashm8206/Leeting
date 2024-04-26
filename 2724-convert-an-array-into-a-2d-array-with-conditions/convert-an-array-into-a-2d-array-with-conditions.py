from collections import defaultdict
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        

        maps = defaultdict(int)

        # Two Pass
        
        # maxFreq = -1

        # for num in nums:
        #    maps[num]+=1
        #    maxFreq = max(maxFreq,maps[num])
        
        # ans = [[] for _ in range(maxFreq)]

        # for num in nums:
        #     idx = maps.get(num)
        #     ans[idx-1].append(num)
        #     maps[num]-=1
        
        # return ans

        # One pass
        ans = []
        for num in nums:
            maps[num]+=1
            freq = maps.get(num)

            # freq --> ans[freq-1]
            # freq > len(ans) # start new array
            # freq == len(ans) --> New Num if encountered, start new array
            if freq > len(ans):
                ans.append([])
            
            ans[freq-1].append(num)
        return ans
            



        

