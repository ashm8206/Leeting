class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_sum = [0]* n
        for i in range(n):
            prefix_sum[i] = arr[i] + (prefix_sum[i-1] if i > 0 else 0)

        result = 0

        for s in range(n):
            for e in range(s+1,n):
                if (e-s+1)%2==1:
                    result+= prefix_sum[e] - (prefix_sum[s-1] if s > 0 else 0)
        print(prefix_sum)
        result+= prefix_sum[n-1]
        return result