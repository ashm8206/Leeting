class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        L = 0
        n = len(nums)
        win_set = set()

        for R in range(n):
            
                # pass

            if nums[R] in win_set:
                return True
            
            win_set.add(nums[R])

            if R-L+1 > k:
                win_set.remove(nums[L])
                L+=1

            # print(win_set)
        return False


