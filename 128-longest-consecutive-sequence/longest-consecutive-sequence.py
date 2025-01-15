class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        hmap = set(nums)

        longest_sec = 0
        curr_seq = 0
        n = len(nums)

        # add another seen sofar set, to avoid duplicate heads
        seen_so_far = set()
        for i in range(n):
            prev = nums[i] - 1
            if prev not in hmap and nums[i] not in seen_so_far:
                nextNum = nums[i]+ 1
                curr_seq = 1
                seen_so_far.add(nums[i])
                while nextNum in hmap:
                    seen_so_far.add(nextNum)
                    curr_seq+=1
                    nextNum +=1
                longest_sec = max(longest_sec,curr_seq)
        return longest_sec

        

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

            
            
