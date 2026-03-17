class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        # nums[i] < nums[k] < nums[j] l .. r
        # nums[j] > nums[k]
        k = float("-inf")
        n = len(nums)
        stack = []
        for i in range(n - 1, -1, -1):
            if nums[i] < k:
                return True

            while stack and stack[-1] < nums[i]:
                # found a higher peak in nums[i] --> j
                k = stack.pop() # previous is a k candidate
                # we want K to be as large as possible
                # maximize changes of getting  j between i .. k
                # so we keep popping

            stack.append(nums[i])
        return False

        

        

        #Approach 
        #  O(n^3)
        # O(n^2) 
        # --> for each j (maxElement)
        # find the minmium uptil "j"
        # to broaden the Range nums[i]..........nums[j]
        # to find a nums[k] between such that nums[i] < num[k] < nums[j]

        # Method I : Brute Force
        # min_i = inf
        # for j in range(len(nums) - 1):
        #     min_i = min(min_i, nums[j])
        #     for k in range(j + 1, len(nums)):
        #         if min_i < nums[k] < nums[j]:
        #             return True
        # return False

        n = len(nums)
        smallest_to_left = [math.inf]*n
        
        for i in range(1,n):
            smallest_to_left[i] = min(smallest_to_left[i-1], nums[i-1])
        
        stack = []

        # 1 < 3 < 2
        # 1.....2 
        #  2 > 3 # 

        #  Now I need to find previous greater, that is > nums[i]
        for i in range(n):

            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
                
            if stack:
                # previousGreater[i] = stack[-1] 
                # previousGreater[nums[k]] = nums[j], viz stack stop

                if smallest_to_left[stack[-1]] < nums[i]:
                    # smallest_to_left[j] ==> nums[i] for this "j"
                    return True

            stack.append(i)
        return False




        
        # 4 - (WinSize) + 1
        
        # 0, 1, 2, 3, 4(x) 4 not included as it is len(s)
        # 4-3 # last eligible index  == 1 winSize = 3
        #  +1 for range func
