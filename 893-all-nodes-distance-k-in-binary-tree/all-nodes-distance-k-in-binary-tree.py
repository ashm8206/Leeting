# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        adjSet= defaultdict(set)
        queue = deque()
        queue.append(root)

        while queue:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
                adjSet[curr.val].add(curr.left.val)
                adjSet[curr.left.val].add(curr.val)
            if curr.right:
                queue.append(curr.right)
                adjSet[curr.val].add(curr.right.val)
                adjSet[curr.right.val].add(curr.val)
        
        queue = deque()
        queue.append((target.val,0))
        visited = set()
        while queue:
            curr, level = queue.popleft()

            visited.add(curr)

            if level==k:
                res.append(curr)

            for nei in adjSet[curr]:
                if nei not in visited:
                    queue.append((nei, level+1))
        return res