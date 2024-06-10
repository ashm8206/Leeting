class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # 2,3,4,1,| 1,3, .....1 |

        L = 0
        maxLen = 0
        hmap = defaultdict(int)
        for R in range(len(nums)):
            hmap[nums[R]]+=1

            while hmap[nums[R]] > k:
                hmap[nums[L]]-=1
                # dont explicitly have to del it
                #  but you can to onverse space complexity
                if hmap[nums[L]] == 0:
                    del hmap[nums[L]]
                L = L + 1
            
            maxLen = max(maxLen, R-L+1)

        return maxLen