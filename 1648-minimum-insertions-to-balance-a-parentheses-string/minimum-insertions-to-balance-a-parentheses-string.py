class Solution:

    def minInsertions(self, s: str) -> int:
        # Keep track of how many closing brackets we need as we iterate through s.
        # These are the invalid states where we need to insert brackets:
        # 1. Odd number of closing brackets required. Requires inserting 1 more close bracket.
        # 2. Negative number of closing brackets required (i.e excess closing brackets). Requires inserting 1 more close bracket if odd. Insert (closing brackets required // 2) opening brackets
        # Handle excess close required brackets at the end of s as well.
        
        closeRequired = 0
        count = 0
        a  = 0
        
        while a < len(s):
            if s[a] == "(":
                closeRequired += 2
                a += 1
            else:
                while a < len(s) and s[a] == ')':
                    closeRequired -= 1
                    a += 1
                                    
                # 1. Positive closeRequired
                # Even closeRequired -> do nothing
                # Odd closeRequired -> insert 1 more close bracket, subtract 2 closeRequired -> insert = 1
                
                # 2. Negative closeRequired 
                # Even closeRequired -> Add closeRequired // 2 open brackets -> closeRequired = 0
                # Odd closeRequired -> Add 1 extra closeRequired and insert [closeRequired //2] open brackets -> closeRequired = 0
                
                if closeRequired > 0:
                    if closeRequired % 2 == 0:
                        continue
                    closeRequired -= 1
                    count += 1
                else:
                    if abs(closeRequired) % 2 == 1:
                        closeRequired -= 1
                        count += 1
                        
                    count += abs(closeRequired) // 2
                    closeRequired = 0
        
        return count + closeRequired
        


        