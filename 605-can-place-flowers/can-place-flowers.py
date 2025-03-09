class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # [1,0,0,0,1, 0, 0]
        # [  x,1 x,x,x,1]

        bedLen = len(flowerbed)

        for i in range(bedLen):
            if flowerbed[i]==0:

                emptyLeft = (i==0) or flowerbed[i-1]==0
                emptyRight = (i==bedLen-1) or flowerbed[i+1]==0

                if emptyLeft and emptyRight:
                    flowerbed[i]=1
                    if n > 0:
                        n-=1
                    if n==0:
                        return True
        return n==0

        # Method II
#         Instead of using that super long 'if condition'. Its better to add 0 at the start and end of the list.
# Makes it cleaner and easier to understand!
        s = len(flowerbed)
        bed = [0] + flowerbed + [0]
        
        for i in range(1, s+1):
            if bed[i] == bed[i-1] == bed[i+1] == 0:
                bed[i] = 1
                n -= 1
            
            if n <= 0: return True
        
        return False