class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        
        while y: # while carry

            answer = x ^ y 
            # XOR: 0+1/1+0, 1+1 = 0, 0+0= 0

            carry = (x & y) << 1 
            #(x & y) detects the 1+1, 
            # which are bound to generate carry 
            # << 1  and shift the 1 by 1 postio to left making it 10
            x, y = answer, carry
        return bin(x)[2:]