class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        numBox = len(boxes)
        res =[0] * numBox
        
        #minimum # Operations per i to move all balls to i
        
        for i in range(numBox):
            for j in range(numBox):
                if i!=j and boxes[j]=='1':
                    res[i]+= abs(j-i)
        return res