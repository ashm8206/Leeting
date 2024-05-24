from collections import deque
# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        
    
        # if root is None:
        #     return None
        
        # queue = collections.deque([root])
        # seen = {}
        # level = 0
        

        # while queue:
        #     node = queue.popleft()
        #     new_node = NodeCopy(node.val)
        #     seen[new_node] = new_node
            

        #     if node.left:
        #         queue.append(node.left)
        #         seen[node.left] = NodeCopy(node.left.val)
        #         new_node.left = seen[node.left]

        #     if node.right:
        #         queue.append(node.right)
        #         seen[node.right] = NodeCopy(node.right.val)
        #         new_node.right = seen[node.right]

        #     if node.random:
        #         seen[node.random] = NodeCopy(node.random.val)
        #         new_node.random = seen[node.random]
            
        #     print(seen[new_node].val)
        #     if seen[new_node].left:
        #         print(new_node.left.val)
        #     if seen[new_node].right:
        #         print(new_node.right.val)
        #     print("-----")
        #     # print(seen[new_node])
        #     # seen[node] = new_node

        #     if level == 0:
        #         new_root = new_node
        #     level+=1
        # return seen[new_root]

        def clone_bt(node):

            if node is None:
                return None
            
            if node in maps: # maps acts like a visited array
                return maps[node]
            
            maps[node] = NodeCopy(node.val)
            maps[node].left = clone_bt(node.left)
            maps[node].right = clone_bt(node.right)
            maps[node].random = clone_bt(node.random)

            return maps[node]

        maps = {}
        new_root = clone_bt(root)
        return new_root
            
            

