class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
    
        tokens.sort()

        left = 0
        right = len(tokens) - 1
        score = 0
        ans = 0
        while left <= right: 
            # each token can be played either way, 
            # when they overlap they can be played either way

            if tokens[left] <= power:
                power -= tokens[left] 
                score+=1
                left+=1

            elif score > 0 and left < right:
                power+= tokens[right]
                right-=1
                score-=1
            else:
                return score

            ans = max(ans, score)

        return ans
            

