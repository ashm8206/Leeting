class Solution:
    def secondHighest(self, s: str) -> int:



        maxSofar = -1
        prev_max = -1

        for char in s:
            if char.isalpha():
                continue
                
            digit = int(char)
            if digit > maxSofar:
                prev_max = maxSofar
                maxSofar = digit

            if digit < maxSofar and digit > prev_max:
                prev_max = digit
                

                # print(digit, maxSofar, prev_max)
        
        if maxSofar==prev_max:
            return maxSofar
        else:
            return prev_max

        