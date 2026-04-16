"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node

        q = deque()
        visited = dict()
        # Append you add
        q.append(node)
        visited[node] = Node(node.val)

        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                if nei not in visited:
                    # same state maintained here
                    visited[nei] = Node(nei.val)
                    q.append(nei)
                # happens wether or not it is visited
                visited[curr].neighbors.append(visited[nei])
        return visited[node]






