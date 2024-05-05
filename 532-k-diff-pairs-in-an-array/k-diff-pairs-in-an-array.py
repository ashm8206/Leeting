class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        hmap = defaultdict(int)
        unique_pairs = set()

        # i = j+k +1 (3+2:5)
        # i = j-k  + 1 (3-2:1)
        

        for num in nums:
            diff1 = num-k
            diff2 = num+k

            if diff1 in hmap:
                unique_pairs.add(min(diff1,num))
            
            if diff2 in hmap:
                unique_pairs.add(min(diff2,num))
        

            hmap[num]+=1
        return len(unique_pairs)
       


