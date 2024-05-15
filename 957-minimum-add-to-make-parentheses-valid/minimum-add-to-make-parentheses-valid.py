class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Can you find the Number of Unbalanced parenthesis and return that?
        
        unbalanced = []
        closed = 0
        for ch in s:
            if ch == '(':
                unbalanced.append('(')
            else:
                if len(unbalanced) > 0:
                    unbalanced.pop()
                else:
                    closed +=1

        return len(unbalanced) + closed

    