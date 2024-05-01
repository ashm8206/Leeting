class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
      
        maps = {}
        ans = 0
        for d in deliciousness:
            for i in range(0,22):
                diff = (1<<i) - d
                
                if diff in maps:
                    # if any diff found, for any of the matching 2**21 powers
                    # add their counts to the answer
                    # next time same value is found
                    # we will account for its previous counts
                    ans+= maps.get(diff,0)
                   
            maps[d] = maps.get(d,0) + 1
        
        return ans % (10**9 + 7)
        
