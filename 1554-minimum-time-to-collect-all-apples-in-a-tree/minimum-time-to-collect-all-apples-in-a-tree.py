class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node, parent):
            res = 0
            for nei in adj_list[node]:
                if nei!=parent:
                    res+= dfs(nei, node)
            # going back bottom up. post-order part
            if node!=0:
                # if current node has apple or children have apples
                if res or hasApple[node]:
                    res+=2 
            return res 


        adj_list = defaultdict(list)
        for u,v in edges: 
            adj_list[u].append(v)
            adj_list[v].append(u)

        return dfs(0, None)