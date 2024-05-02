class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        # hmap = defaultdict(list)

        # for i, num in enumerate(nums):
        #     hmap[num].append[i]
        
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    count+=1
        return count

