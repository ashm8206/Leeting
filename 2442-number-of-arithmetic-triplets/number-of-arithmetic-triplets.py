class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        n = len(nums)
        count = 0
        # for i in range(n-2):
        #     for j in range(i+1,n-1):
        #         if nums[j]-nums[i]==diff:
        #             for k in range(j+1,n):
        #                 if nums[k]-nums[j]==diff:
        #                     count+=1
        # return count
        
        #  if there is 1 number nums[i]
        #  such that nums[i]+diff in map and nums[i]+diff +diff in map
        # Triplet found, increment count

        # They used substitution to solve

        # nums[j]   == diff + nums[i]
        # nums[k] ==  diff + diff + nums[i]

        maps = set()

        for num in nums:
            maps.add(num)
        
        for num in nums:
            if num+diff in maps and num+diff+diff in maps:
                count +=1
        return count
        # https://leetcode.com/problems/number-of-arithmetic-triplets/solutions/4654949/beats-100-of-users-step-by-step-explain-using-hashmap-easy-to-understand/
