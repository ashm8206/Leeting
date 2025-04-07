class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}
        def helper(left, right, turn):
            if left > right:
                return 0

            if (left, right, turn) in memo:
                return memo[(left, right, turn)]
            
            res = 0
            if turn == 1:
                res = max(piles[left]+helper(left+1, right, 2), piles[right]+helper(left, right-1, 2))
            else:
                # try an minimize turn 1 score

                res = min(helper(left+1, right, 1), helper(left, right-1, 1))
            memo[(left, right, turn)] = res
            return res
        
        n = len(piles)
        alice_score = helper(0,n-1, 1)
        bob_score = sum(piles) - alice_score
        return bob_score < alice_score

            