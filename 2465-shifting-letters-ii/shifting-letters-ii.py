class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        diff_array = [0] * (n+1)  # Initialize a difference array with all elements set to 0

       

        # Process each shift operation
        for l, r, d in shifts:
            diff_array[r+1] += 1 if d else -1
            diff_array[l] += -1 if d else 1
        
        res = [ ord(c) - ord("a") for c in s ]
        diff = 0

        # Apply the shifts to the string
        for i in range(len(diff_array)-1,-1,-1):
            diff += diff_array[i]

            res[i-1] = (diff + res[i-1]) % 26  
            # Update cumulative shifts, keeping within the alphabet range
           

            
            
        result = [chr(ordnum + ord("a")) for ordnum in res]
        return "".join(result)