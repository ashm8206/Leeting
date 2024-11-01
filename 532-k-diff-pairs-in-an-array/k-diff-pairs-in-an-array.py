class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        hmap = defaultdict(int) 

        unique_pairs = set()


        for num in nums:
            diff1 = num-k
            diff2 = num+k

            if diff1 in hmap:
                unique_pairs.add(min(diff1,num))
            
            if diff2 in hmap:
                unique_pairs.add(min(diff2,num))
        

            hmap[num]+=1
        return len(unique_pairs)

        # Method I - NlogN
        
        # nums.sort()
        
        # n = len(nums)

        # hmap = defaultdict(int)
        # ans = 0
        # for i in range(n):
        #     if k > 0 and i > 0 and nums[i]==nums[i-1]:
        #         continue

        #     if k==0 and hmap[nums[i]]==2 and nums[i]==nums[i-1]:
        #         continue

        #     diff1 = nums[i] - k
        #     diff2 = nums[i] + k

        #     if diff1==diff2:
        #         ans += hmap[diff1]
        #     else:
        #         ans += hmap[diff1]
        #         ans += hmap[diff2]

        #     hmap[nums[i]] += 1
        # return ans
