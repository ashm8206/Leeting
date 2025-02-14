from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # remainder = defaultdict(int)

        # # Distributive mod
        # # (a + b) mod = (a/mod + b/mod) % mod
        # count = 0
        # for t in time:
        #     if (t%60)==0:
        #         count += remainder[0]
        #     else:
        #         count+= remainder[60-t%60]
        #     remainder[t%60]+=1
        # # print(remainder)
        # return count

    # Mix of two Sum, +  Number of Good Pairs 
    # (a+b)%60 i.e 
        # 1. both are divisble by 60 R1 = 0
        # 2. or their pair divisble sum = 60 
    # i.e a%60  + b%60 = 60

        hmap = {}
        count = 0

        for num in time:
            key = num%60

            if key == 0:
                count+= hmap.get(key,0) # both are divisible, so get 0
            else:
                count+=hmap.get(60-key,0) # diff = b%60

            hmap[key] = hmap.get(key,0) + 1
        return count
