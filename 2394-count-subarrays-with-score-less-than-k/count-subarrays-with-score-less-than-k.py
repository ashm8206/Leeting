class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        psum = [0]+list(accumulate(nums))
        ans = i = 0
        for j in range(len(psum)):
            while (psum[j] - psum[i])*(j-i)>=k:
                i += 1
            ans += (j-i)
        return ans