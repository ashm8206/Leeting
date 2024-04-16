class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        # you don't have to compute all operations
        # since All operations are indexed from 0,0, (x1,x2) Overlap is guaranteed
        # Now we need to min the min(x1, y1)  and multiply them to H*W = Area == COUNT
        
        minX = 10**5
        minY = 10**5
        for x, y in ops:
            minX, minY = min(minX,x), min(minY,y)
        # print(minX,minY)
        return minX*minY if len(ops) > 0 else m*n
