class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_idx = {}
        count = {}
        res = 0
        degree = 0

        for i, a in enumerate(nums):
            first_idx.setdefault(a,i)
            count[a] = count.get(a,0) + 1
            if count[a] > degree:
                degree = count[a]
                res = i - first_idx[a] + 1
            elif count[a] == degree:
                res = min(res, i - first_idx[a] + 1)
        return res
        








        counts = collections.defaultdict(int)
        for val in nums:
            counts[val]+=1

        degree = max(counts.values())

        # find start and end for thoses Keys whose value == key
        left = {}
        right = {}
        n = len(nums)
        for i in range(n):
            
            if nums[i] not in left and counts[nums[i]]==degree:
                    left[nums[i]] = i
            if nums[n-1-i] not in right and counts[nums[n-1-i]]==degree:
                    right[nums[n-1-i]]= n-1-i
    
        minSubArray = 10**5
        for key, val in left.items():
            
            minSubArray = min(minSubArray, right[key]-left[key]+1)
        
        return minSubArray
            
