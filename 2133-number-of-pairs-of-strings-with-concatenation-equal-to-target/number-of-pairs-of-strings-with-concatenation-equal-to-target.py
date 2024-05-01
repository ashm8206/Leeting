class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        hmap = {}
        # maps = set(nums)

        ans = 0
        for i, num in enumerate(nums):
            prefix = target[:len(target)-len(num)]

            if prefix in hmap and prefix + num == target:
                ans += hmap.get(prefix, 0)

            
            # When Numbers are the same, 
            # you Gotta check for the suffix
            suffix = target[len(num):]
            if suffix in hmap and  num + suffix == target:
                ans += hmap.get(suffix, 0)
    
            hmap[num] = hmap.get(num, 0) + 1
        return ans