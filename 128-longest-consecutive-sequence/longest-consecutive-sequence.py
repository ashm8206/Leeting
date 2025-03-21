class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        longest_streak = 0
        num_set = set(nums)
        # this avoids including numbers part of other sequences
        for num in num_set: 
            
            if num - 1 not in num_set: # potential head
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

        

        # nums.sort()
        # # print(nums)

        # n = len(nums)
        # if n <= 1:
        #     return n
        
        # longSoFar = 1 
        # consectSec = 1

        # for i in range(1,n):
        #     if nums[i-1] + 1 == nums[i]:
        #         consectSec+=1 
        #     elif nums[i-1] == nums[i]:
        #         continue
        #     else:
        #         consectSec = 1
           
        #     longSoFar = max(longSoFar, consectSec)
        #     # print(longSoFar)

        # return longSoFar

        # # Len of Nums 0,1 --> loop(1,n)
        # # duplicates
        # # [0,0]

        #Optimal Method
        # 1. find the head of the seq:
            #  the head of the seq 
            # wont have its preceeding number in the Hash Map
        # Once this head is found
        # Keep searching for the next number

        # 100, 4, 3 ,200, 2, 1, 

        searchSet = set(nums)


        n = len(nums)

        longSoFar = 0 
        consectSec = 1

        
        for num in nums:
            prev = num - 1 
            if prev not in searchSet:
                # seen.add(num)
                nextNum = num+1
                consectSec = 1
                while nextNum in searchSet:
                    # and nextNum not in seen
                    # seen.add(nextNum)
                    consectSec+=1
                    nextNum = nextNum+1
                longSoFar = max(longSoFar,consectSec)
        
        return longSoFar

            
            
