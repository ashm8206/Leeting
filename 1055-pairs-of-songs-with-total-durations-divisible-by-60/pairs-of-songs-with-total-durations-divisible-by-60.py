from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # remainder = defaultdict(int)

        

 

        hmap = {}
        count = 0
        # Mix of two Sum, +  Number of Good Pairs 
        # Distributive mod
        #  (a + b) % K = (a%k + b%k) % k

        for num in time:
            #  Vanilla Two Sum
            #  key = target - num:

            # Two sum Divisible pair?
            # find a in hmap ?
            # b ==> num
            # (a+b)%60 = 0 
            # (a%60  + b%60)%60 = 0
            #  Two cases
                # 1. a%60  + b%60 = 0  
                #       i.e since only positve vals, the both a%60 == b%60 = 0 
                #       i.e key = 0
                # 2. a%60  + b%60 = 60

                #  OR  a%60 = 60 - B%60
            # HENCE TWO CASES!!!
        

            key = num%60

            if key == 0:
                count+= hmap.get(key,0) # both are divisible, so get 0
            else:
                count+=hmap.get(60-key,0) # key = b%60

            hmap[key] = hmap.get(key,0) + 1
        return count
