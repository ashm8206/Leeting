class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # Brute Force
        # cnt = 0
        # n = len(nums)
        # for i in range(n-k+1):
        #     if nums[i] == 0 :
        #         for j in range(k):
        #             nums[i+j] = nums[i+j]^1
            
        #         cnt+=1
        #     # print(nums)
        
        # return cnt if sum(nums)== len(nums) else -1

        # Queue
        # n = len(nums)
        # q = deque()
        # res = 0

        # for i in range(n):

        #     while q and q[0] <= i-k:
        #         q.popleft()

           
            

        #     if(nums[i]+ len(q)) % 2 == 0:
        #         # calculate true value based on previous Flips
        #         # odd number of Flips : same val
        #         # even number of Flips: different val

        #         res+=1
        #         q.append(i)
        #          # if true val==0 as is here we need to flip this

        #         if i+k - 1 >= n:
        #             # Are we at an invalid index ?

        #             # i is 0 and  i >= n-k+1
        #             return -1

        # return res

        # Constant space
        n = len(nums)
        validFlips = 0
        res = 0

        for i in range(n):

            if i-k >=0 and  nums[i-k]==2:
                validFlips-=1

           
            if(nums[i]+ validFlips) % 2 == 0:
                # calculate true value based on previous Flips
                # odd number of Flips : same val
                # even number of Flips: different val

                res+=1
                validFlips+=1
                nums[i] = 2
                 # if true val==0 as is here we need to flip this

                if i+k - 1 >= n:
                    # Are we at an invalid index ?
                    
                    # i is 0 and  i >= n-k+1
                    return -1

        return res
