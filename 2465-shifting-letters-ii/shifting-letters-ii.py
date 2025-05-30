from itertools import accumulate
class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        delta = [0] *(n+1)

        for st, end, d in shifts:
            if d==1:
                delta[st]+=  1 
                delta[end+1]+= -1 
            else:
                delta[st]+=  -1 # +d
                delta[end+1]+= 1 #- d
        
        delta = list(accumulate(delta))
        
    
        for i, ch in enumerate(s):
            char_num = (ord(ch) - ord("a") + delta[i] + 26) % 26 +  ord("a")
            delta[i] = chr(char_num)
      

        return "".join(delta[:n])
    













        # n = len(s)
        # diff_array = [0] * (n + 1)  # Initialize a difference array with all elements set to 0

        # # Process each shift operation in forward direction
        # for l, r, d in shifts:
        #     diff_array[l] += 1 if d > 0 else -1  # Start the shift at 'l'
        #     diff_array[r + 1] += -1 if d > 0 else 1  # End the shift at 'r'

        # res = [ord(c) - ord("a") for c in s]  # Convert string to list of character indices (0 to 25)
        # diff = 0  # This will hold the cumulative shift applied to each character

        # # Apply the shifts to the string in a forward pass
        # for i in range(n):
        #     diff += diff_array[i]  # Update the cumulative shift for the current character
        #     res[i] = (res[i] + diff) % 26  # Apply the shift and ensure it's within 'a' to 'z'

        # # Convert the resulting character indices back to characters and join them into a string
        # result = ''.join(chr(ord('a') + r) for r in res)
        # return result


