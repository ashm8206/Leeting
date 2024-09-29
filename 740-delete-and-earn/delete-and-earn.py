from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:


        # Method I
        # n = len(nums)
        # if (n == 0):
        #     return 0
        # if (n == 1):
        #     return nums[0]
        
        # nums.sort()
        # dp = [ nums[i] for i in range(n)]

        # result = nums[0]

        # for i in range(n):
        #     for j in range(0,i):
        #         if (nums[i] == nums[j] or nums[i] > nums[j] + 1):
        #             # print(i, j)
        #             # House robber-ish
        #             #  nums[i] > nums[j] + 1, then add it 

        #             dp[i] = max(dp[i], dp[j] + nums[i])
        
        #     result = max(result, dp[i])
                
        # # print(dp)
        # return result

        points = defaultdict(int)
        max_number = 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        
        @cache
        def max_points(num):
            # Check for base cases
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            
            # Apply recurrence relation
            return max(max_points(num - 1), max_points(num - 2) + points[num])
        
        return max_points(max_number)



        # https://www.youtube.com/watch?v=7FCemBxvGw0
        # counts = Counter(nums)
        # nums = sorted(list(set(nums)))

        # earn1 , earn2 = 0, 0

        # for i in range(len(nums)):

        #     currEarn = nums[i]*counts[nums[i]]

        #     if i > 0 and nums[i]==nums[i-1]+1:
        #         temp = earn2
        #         earn2 = max(currEarn+earn1,earn2)
        #         earn1 = temp
        #     else:
        #         temp = earn2
        #         earn2 = currEarn+ earn2
        #         earn1 = temp # moves to what was previously earn2
        # return earn2

        # [1 ,2, 3]
        #  e1,e2