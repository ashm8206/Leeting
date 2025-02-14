class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #  Bucket Sort for Small range number [0,2]
        # Time Complexity O(n), Space : O(1) --> hmap is constant space, doesnt grow with input
        #  It will be in-place, cuz yo over write the Array based on Hmap

        # Method I Bucket sort
        # hmap = {0:0, 1:0, 2:0}

        # for num in nums:
        #     hmap[num]+=1
        
        # index = 0
        # for key in range(0,3):
        #     while hmap[key]:
        #         nums[index] = key
        #         hmap[key]-=1
        #         index+=1
        # return nums

        # Method II - One pass Two Pointer
        n = len(nums)

        zeroPtr = 0
        twoPtr = n-1
        runner = 0

        while runner <= twoPtr:

            if nums[runner]==0:
                nums[zeroPtr],nums[runner] = nums[runner], nums[zeroPtr]
                zeroPtr+=1

                # zeroPtr will not be 0, and not 2 as 2 is swapped, so it will point to starting of 1
                # twoPtr could be pointing at anything

                runner+=1

            elif nums[runner]==2:
                
                nums[twoPtr],nums[runner] = nums[runner], nums[twoPtr]
                twoPtr -=1
                # runner+=1

                # Dont move runner by 1 
                # As what is swapped might be zero,
                # which has to keep our invariant
                # 
                #  # <-- zeroPtr : 0
                # twoPtr ---> : 2

                

            else:
                # encounters 1 so increment.
                runner +=1

        return nums




            


