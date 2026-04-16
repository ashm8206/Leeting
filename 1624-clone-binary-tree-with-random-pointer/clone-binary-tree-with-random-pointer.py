from collections import deque
# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

from collections import deque
class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        
    
        if root is None:
            return None
        
        queue = deque()
        seen = {} # DICT , not for cycles, in BST, but for quick access
        

        queue.append(root)
        seen[(root)] = NodeCopy(root.val)
    



        while queue:
            node = queue.popleft()

            if node.left:
                
                queue.append(node.left)
                seen[node.left] = NodeCopy(node.left.val)
                seen[node].left = seen[node.left]
        

            if node.right:
                queue.append(node.right)
                seen[node.right] = NodeCopy(node.right.val)
                seen[node].right = seen[node.right]
            
            
        # Pass 2   
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            
            if curr.random is not None:
                # Point to the COPY, not the original node
                seen[curr].random = seen[curr.random]
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        return seen[root]


        # def clone_bt(node):

        #     if node is None:
        #         return None
            
        #     if node in maps: # maps acts like a visited array
        #         return maps[node]

        #     # set in map as PreOrder incase the random ptrs points bck
        #     # this avoids maximum recursion exceeded.
        #     maps[node] = NodeCopy(node.val)
        
        #     maps[node].left = clone_bt(node.left)
        #     maps[node].right = clone_bt(node.right)
        #     maps[node].random = clone_bt(node.random)

        #     return maps[node]

        # maps = {}
        # new_root = clone_bt(root)
        # return new_root
            
        # https://leetcode.com/problems/clone-binary-tree-with-random-pointer/solutions/742100/python-recursive-iterative-dfs/

