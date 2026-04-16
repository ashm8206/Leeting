"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""
from collections import deque
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':

        if not root:
            return root
        visited = dict()
        q = deque()
        q.append(root)
        visited[root] = Node(root.val)

        while q:
            curr = q.popleft()

            for child in curr.children:
                if child not in visited:
                    visited[child] = Node(child.val)
                    q.append(child)
                # clone node's children
                visited[curr].children.append(visited[child])
        return visited[root]