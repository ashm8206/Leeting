class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        n = len(wordsDict)

        # w1 = 0
        # w2 = 0

        minDist = 10**9
        # for i in range(n):
        #     if wordsDict[i]==word1:
        #         print(wordsDict[i])
        #         for j in range(n):
        #             if wordsDict[j]==word2:
        #                 minDist = min(minDist, abs(i-j))

        w1 = -1
        w2 = -1

        for i in range(n):
            if wordsDict[i]==word1:
                w1=i
            if wordsDict[i]==word2:
                w2=i

            if w1!=-1 and w2!=-1:
                minDist = min(minDist,abs(w1-w2))

            # We only care about the closests w1 and w2 ptrs
            # All combinations are not neccesaary
        return minDist

        