class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        #directly or indirectly connected sounds like an island problems
        #going to treat grid[1][1] == 1

        count = 0
        n = len(isConnected)
        seen= set()
        def dfs(u):
            seen.add(u)
            for v in range(n):
                if v not in seen and isConnected[u][v] == 1 :
                    dfs(v)

        
        for u in range(n):
            if u not in seen:
                dfs(u)
                count+=1
        return count

        
        # for u in range(n):
        #     if u not in seen:
        #         dfs(u)
        #         count +=1 
        # return count

