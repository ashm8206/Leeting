class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # find the brute Force first:
        # logic behind 0..n and 0..n vs i+1..n in second loop
        
        # [0,1, 2]
        # [1,0, 0]
        
        balls_to_left = 0
        moves_to_left = 0

        balls_to_right = 0
        moves_to_right = 0
        n = len(boxes)
        res = [0] * n


    # Each time we move to the next box, the distance for all the balls we’ve passed increases by one. So, the total number of operations for those balls increases by the number of balls we've encountered up to that point. 

        for i in range(n):
            # Left side
            res[i]+= moves_to_left
            balls_to_left += int(boxes[i])
            moves_to_left += balls_to_left

            # print(i, res[i],balls_to_left, moves_to_left)
            
        
            j = n - i -1

            res[j]+= moves_to_right
            balls_to_right += int(boxes[j])
            moves_to_right += balls_to_right
        return res

            










        # numBox = len(boxes)
        # res =[0] * numBox
        
        # #minimum # Operations per i to move all balls to i
        
        # for i in range(numBox):
        #     for j in range(numBox):
        #         if i!=j and boxes[j]=='1':
        #             res[i]+= abs(j-i)
        # return res