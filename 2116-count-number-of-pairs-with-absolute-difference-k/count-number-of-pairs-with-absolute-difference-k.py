class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hmap = {}
        ans = 0
        for num in nums:
            
            diff1 = num + k
            diff2 = num - k

            ans += hmap.get(diff1, 0)
            ans += hmap.get(diff2, 0)
            # Get the number of times this diff has occured before,
            # If it has occured N times, It will make N pairs with THIS number
        
            hmap[num] = hmap.get(num, 0) + 1
            # Insert number in the map for future differences
        return ans

        # 2
        
        # -1: 1
        # 1: 1