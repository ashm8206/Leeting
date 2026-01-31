class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
       
        n = len(nums)
        if n < 3:
            return float('inf')  # Not possible with less than 3 elements
        
        # Find longest increasing subsequence from left
        def getLIS(arr):
            sub = []
            dp = [1] * len(arr)  # Length of LIS ending at each index
            
            for i, num in enumerate(arr):
                pos = bisect_left(sub, num)
                if pos == len(sub):
                    sub.append(num)
                else:
                    sub[pos] = num
                dp[i] = pos + 1  # Store length of LIS ending at i
            return dp
        
        # Get LIS from left to right and right to left
        left_lis = getLIS(nums)
        right_lis = getLIS(nums[::-1])[::-1]  # Reverse array for decreasing sequence

        print(left_lis, right_lis)

       
        min_removals = float('inf')
        # Try each index as peak
        for i in range(1, n-1):  # Peak can't be at ends
            
            if left_lis[i] > 1 and right_lis[i] > 1:
            # they have to have atleast 2 element including peak 
            # both of them to form a mountain array with 3 elems
            
                total_length = left_lis[i] + right_lis[i] - 1  
                # -1 because peak is counted twice
                removals = n - total_length
                min_removals = min(min_removals, removals)
                
        return min_removals if min_removals != float('inf') else -1