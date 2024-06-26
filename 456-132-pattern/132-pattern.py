class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # 0, 1, 2
        # 1 < 4 > 2
        #  1st for minimum array from left  every minimum number : i 
        # find the 2nd from the right  next Greater  == k 
        # if there exists a sma

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

            if stack: # 3 element 
                
                if nums[potentialOnes[stack[-1]]] < nums[i]:
                    # check the 1st element at that position from PotentialOnes
                    # if it is < the currElement
                    #  Then we found a 1 - 3 - 2 pair

                    # the 3-2 pair is valid beacuse if the number of was greater or equal
                    # it would've displaced the currMax element in stack 
                    # by default curr[i] will either displace stack or  it is  > stack[-1]
                    return True
            
            stack.append(i)
    
        return False
