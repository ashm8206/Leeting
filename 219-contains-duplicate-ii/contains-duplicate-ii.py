class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        L = 0
        n = len(nums)
        win_set = set()

        for R in range(n):

            if R-L > k:  # abs(i-j) window size = R-L
                win_set.remove(nums[L])
                L+=1
                
            
            if nums[R] in win_set:
                return True
            
            win_set.add(nums[R])

            
        return False


