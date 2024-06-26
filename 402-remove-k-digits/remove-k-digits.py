class Solution:
    def removeKdigits(self, num: str, k: int) -> str:



        numStack = []
        
        # Construct a monotonic strictly increasing sequence of digits
        for digit in num:

            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
            numStack.append(digit)
        
        # Test Cases
        # 112 --> 11, not 12
        #  9 --> 0

        if k: # not fully spent as in case of 112
            numStack = numStack[:-k]
        
        return "".join(numStack).lstrip('0') or "0"
     

        
        
        # # - Trunk the remaining K digits at the end
        # # - in the case k==0: return the entire list
        # finalStack = numStack[:-k] if k else numStack
        
        # # trip the leading zeros
        # return "".join(finalStack).lstrip('0') or "0"