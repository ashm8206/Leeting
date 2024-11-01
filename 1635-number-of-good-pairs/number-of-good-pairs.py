class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #In general, whenever we encounter a number, it can form k good pairs with previously traversed numbers, 
        # where k is the number of times we have seen the number previously.
        # hmap= {}
        # ans = 0
        # for num in nums:
        #     ans += hmap.get(num,0)
        #     hmap[num]= hmap.get(num,0)+ 1
        # return ans

        ans = 0
        hmap = defaultdict(int)
        for num in nums:
            # if num in hmap:   
                # num ==1 and '1' seen 3 times before
                # this 1 can form 3 pairs with previously see 1s
            ans+= hmap[num]

            hmap[num]+= 1
        return ans
