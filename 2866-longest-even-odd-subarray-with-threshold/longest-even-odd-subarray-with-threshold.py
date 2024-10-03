class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int: 
        
        # msf = 1 
        

        start_even = True if nums[0]%2==0 else False

        cmax = 1 if nums[0] <= threshold and start_even else 0
        
        msf =  cmax

        n = len(nums)
        

        for i in range(1,n):
            
            if start_even and nums[i]%2!=nums[i-1]%2 and nums[i] <= threshold and nums[i-1]<=threshold:
                cmax +=1
             
            else:
                start_even = True if nums[i]%2==0 else False
                cmax = 1  if nums[i] <= threshold and start_even else 0
                
            msf = max(msf, cmax)
            print(msf, nums[i])
        return msf
        