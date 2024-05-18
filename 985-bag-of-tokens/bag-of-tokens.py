class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
    
        tokens.sort()

        left = 0
        right = len(tokens) - 1
        score = 0
        ans = 0
        while left <= right: 
            # each token can be played either way, 
            # when i/j overlap they can be played either way but not both

            if tokens[left] <= power:
                power -= tokens[left] 
                score+=1
                left+=1

            elif score > 0 and left < right:
                # can't double count
                score-=1
                power+= tokens[right]
                right-=1
                
            else:
                # i==j and no more smaller power or score == 0 
                print('--')
                return score

            print(left, right)
        return score
            

