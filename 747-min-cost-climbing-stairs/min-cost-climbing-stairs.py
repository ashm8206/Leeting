class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) #[0..n-1]
        minCost = [0]*(n+1)



        """ Notes: Draw the stairs, bottom Floor + Top Floor cost as 0
        these are additional Stairs appended in drawing.

        Bottom stair, not req in DP array, but Top stair required,
        minCost[N+1] = mininum Cost required to reach this index
        """

        # Start iteration from step 2, since the minimum cost of reaching
        # step 0 and step 1 is 0
    
        # Now we solve problems iwth Optimal sunstructure, small problems optimallly that lead to our answer found at N+1 

        for i in range(2, n+1):
            # take one step from previous step to reach here
            take_one_step = minCost[i-1] + cost[i-1]

            # take 2 Steps from prev's prev  to reach here

            """Understanding

                # eg: [10,15, 5, 1, 2, 4, 20]

            #  To reach idx 6 (viz still not the top btw: top = idx 7)
            # 1. we can take 2 steps from idx 4
            # 2. we can take 1 step from idx 5

            1. Even if we take 2 steps from idx 4,

            We pay cost = minCost[4] + cost[4]
            We don't pay cost[4]2x if we take 2 steps
            We don't pay cost[4] + cost[5] if we take 2 steps
            We only pay cost[4] once!

            2. We cant take 2 steps from idx 5, to reach 6. 
            If we take 2 steps from idx 5, we will overshoot and reach 7
            we will never reach 6. 
            This problem is solved later when filling table
            
            """

            take_two_step = minCost[i-2] + cost[i-2] 
            minCost[i] = min(take_one_step, take_two_step)
        
        # print(minCost) --> [0, 0, 10, 15]
        return minCost[n]
      





        