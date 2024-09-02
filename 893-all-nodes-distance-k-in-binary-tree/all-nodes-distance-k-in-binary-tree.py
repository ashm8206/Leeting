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

        # Alternative - Build parent pointers
        graph = collections.defaultdict(list)
        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur) 
        build_graph(root, None)

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
                continue
            for nei in adjSet[curr]:
                if nei not in visited:
                    queue.append((nei, level+1))
        return res