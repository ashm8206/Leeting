class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # [1,0,0,0,1, 0, 0]
        # [  x,1 x,x,x,1]

        bedLen = len(flowerbed)
        count = 0

        for i in range(bedLen):
            if flowerbed[i]==0:

                emptyLeft = (i==0) or flowerbed[i-1]==0
                emptyRight = (i==bedLen-1) or flowerbed[i+1]==0

                if emptyLeft and emptyRight:
                    flowerbed[i]=1
                    count+=1

        return count>=n