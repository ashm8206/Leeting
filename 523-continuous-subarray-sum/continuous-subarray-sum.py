class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        # Neetcode #https://www.youtube.com/watch?v=OKcrLfR-8mE
        hmap = {0: -1} # we have seen 0%k --> 0 at -1 index
        curr_sum = 0
        n = len(nums)

        for i in range(n):
            curr_sum+= nums[i]
            key = curr_sum % k

            # curr_sum = (curr_sum + nums[i]) % k

            # (prefix[j] - prefix[i])%k = 0
            #  or prefix[j]%k = prefix[i]%k
            if key in hmap.keys():
                if i - hmap[key] >= 2:
                    return True
                # At this place we must not change the remainder index
                # if second Condition is not met
                # Test Case: [5,0,0,0,0], k = 3
            else:
                hmap[key] = i
        return False

        