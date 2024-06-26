class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # i, j,  k
        # 1 < 4 > 2

        #Approach 
        #  O(n^3)
        # O(n^2) 
        # --> for each j (maxElement)
        # find the minmium uptil "j"
        # to broaden the Range nums[i]..........nums[j]
        # to find a nums[k] between such that nums[i] < num[k] < nums[j]

        n = len(nums)
        stack = []
        potentialOnes = [10**10]*n


        for i in range(n):

            if i==0:
                potentialOnes[i] = 0
            elif nums[i] < nums[potentialOnes[i-1]]:
                potentialOnes[i] = i
            else:
                potentialOnes[i] = potentialOnes[i-1]


            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack: # 3 element or "j", the new element hasnt displaced it
                
                if nums[potentialOnes[stack[-1]]] < nums[i]:
                    # get "1" or "i"
                    # going to index 3 in PotentialOnes to get index of 1 
                    # and find that index in nums to get "i"
                    # compare to current element or nums[i]== k or "2"
                    return True
            
            stack.append(i)
    
        return False

        # 4 - (WinSize) + 1
        
        # 0, 1, 2, 3, 4(x) 4 not included as it is len(s)
        # 4-3 # last eligible index  == 1 winSize = 3
        #  +1 for range func
