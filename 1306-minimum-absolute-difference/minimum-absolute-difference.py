class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort() # important
        minimum = float("inf")
        n = len(arr)
        ans = []
        for i in range(1, n):
            current = arr[i] - arr[i-1]
            if current < minimum:
                ans = [[arr[i-1], arr[i]]]
                minimum = current
            elif current == minimum :
                ans.append([arr[i-1], arr[i]])
        return ans
