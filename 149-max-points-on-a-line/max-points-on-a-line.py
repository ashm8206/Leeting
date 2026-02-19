import math
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n==1:
            return 1
        count = float("-inf")

        for i in range(n):
            x1 = points[i][0]
            y1 = points[i][1]

            repeated = 1
            slope = defaultdict(int)
            maxpoints = float("-inf")

            for j in range(i+1, n):

                x2 = points[j][0]
                y2 = points[j][1]
                
                if(x1==x2 and y1==y2):
                    repeated+=1
                    continue
                
                dx = x2-x1
                dy = y2-y1

                # Gcd to requried to treat 2/4, same as  5/10
                g = math.gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                    # if dx -ve,  
                    # flip both signs to preserve slope
                    # (-4,2) --> (4,-2)
                    # (-4,-2) --> (4,2)
                    # This condition handles horizontal lines as well.

                    # No vertical lines need to be handled seperately..
                    # dx==0 and dy < 0 : then count it as same slope

                
                key = (dx,dy)
                slope[key]+= 1
                maxpoints = max(maxpoints, slope[key])
            count = max(count, (maxpoints + repeated))
        return count

        # private int gcd(int big, int small){
        # if(small == 0) return big;
        # return gcd(small, big%small);
    # }