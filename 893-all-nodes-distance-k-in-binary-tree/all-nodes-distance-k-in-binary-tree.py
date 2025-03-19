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
        def build_graph(curr, parent):
            if curr:
                graph[curr].append(parent)
                graph[parent].append(curr)
            if curr.left:
                build_graph(curr.left, curr)
            if curr.right:
                build_graph(curr.right, curr) 
        build_graph(root, None)

        # while queue:
        #     curr = queue.popleft()
        #     if curr.left:
        #         queue.append(curr.left)
        #         adjSet[curr.val].add(curr.left.val)
        #         adjSet[curr.left.val].add(curr.val)
        #     if curr.right:
        #         queue.append(curr.right)
        #         adjSet[curr.val].add(curr.right.val)
        #         adjSet[curr.right.val].add(curr.val)
        
        queue = deque()
        queue.append((target,0))
        visited = set()
        while queue:
            curr, level = queue.popleft()

            visited.add(curr)

            if level==k:
                if curr:
                    res.append(curr.val)
                # continue
            # for nei in adjSet[curr]:
            for nei in graph[curr]:
                if nei not in visited:
                    queue.append((nei, level+1))
        return res