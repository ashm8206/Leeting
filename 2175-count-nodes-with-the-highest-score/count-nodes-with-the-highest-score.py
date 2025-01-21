class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        children = defaultdict(list)
        
        for node, parent in enumerate(parents):
            children[parent].append(node)
        
        freq = defaultdict(int)
        NODES = len(parents)
        
        # Idea is when we remove a node, we split it into, three parts,
        # 1. The left subtree(left) 
        # 2. The right subtree (right) 
        # 3. All other nodes connected to it's parent (up)
        def dfs(node):
            left = right = 0
            if children[node]: # Count left subtree, it is binary tree so we can index 0/1 for left/right
                left = dfs(children[node][0])
            if len(children[node]) > 1: # Count right subtree
                right = dfs(children[node][1])
            up = NODES - left - right - 1 # Count nodes connected to parent
            # short-circuiting, becomes 1 if expr evaluates to 0
            score = (left or 1) * (right or 1) * (up or 1)
            freq[score] += 1
            return 1 + left + right
        
        dfs(0)
        # max to get frequency of max score
        return freq[max(freq)] 