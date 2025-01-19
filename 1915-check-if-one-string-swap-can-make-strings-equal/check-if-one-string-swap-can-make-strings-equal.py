class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        countsA = [0]*26
        countsB = [0]*26
        mismatch = 0
        for a, b in zip(s1, s2):
            idxA = ord(a) - ord("a")
            idxB = ord(b) - ord("a")
            countsA[idxA]+=1
            countsB[idxB]+=1

            if a!=b:
                mismatch+=1
        
    
        if countsA == countsB and mismatch in (2, 0):
            return True
        return False
        