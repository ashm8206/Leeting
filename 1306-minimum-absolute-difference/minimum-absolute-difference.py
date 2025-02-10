class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum = float("inf")
        n = len(arr)
        for i in range(1, n):
            current = arr[i] - arr[i-1]
            if current < minimum:
                minimum = current
        
        ans = []
        for i in range(1, n):
            if arr[i] - arr[i-1] == minimum:
                ans.append([arr[i-1], arr[i]])
        return ans
