class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = [(ag,sc) for sc, ag in zip(scores, ages)]

        arr.sort(key = lambda x: (x[0],x[1]) )

        n = len(arr)
        dp = [arr[i][1] for i in range(n)]
        maxScore = arr[0][1]

        for i in range(1, n):
            for j in range(0, i):
                if arr[j][1] <= arr[i][1]:
                    dp[i] = max(dp[i], dp[j]+arr[i][1])
            maxScore = max(maxScore, dp[i])
        return maxScore