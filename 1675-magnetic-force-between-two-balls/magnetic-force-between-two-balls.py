class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        
        # in this problem although niot explicit said
        # adjaceny matters

        # For example, if positions were [10, 1, 5, 8], without sorting, your algorithm would consider adjacent positions as 10→1, 1→5, 5→8, which doesn't represent their actual order on the number line.
# 
        def count(d):
            ans = 1
            curr = position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans
        
        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = (l+r+1)//2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l