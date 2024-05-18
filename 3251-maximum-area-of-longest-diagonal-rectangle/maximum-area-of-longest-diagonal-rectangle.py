class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiag = 0
        maxArea = 0
        for l, w in dimensions:
            currDiag = l**2 + w**2
            if maxDiag < currDiag:
                # print(maxDiag, currDiag, maxArea, l*w)
                maxDiag = currDiag
                maxArea = l * w
                
            
            if maxDiag == currDiag:
                maxArea = max(l*w, maxArea)
        return maxArea


        9,3
