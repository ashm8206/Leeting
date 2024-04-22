"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return root
        
        queue = collections.deque()

        queue.append(root)

        while queue:
            length = len(queue)

            # print(length)
            for i in range(length):
                
                node = queue.popleft()

                # print(node.val)
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                if  i < length - 1:
                    next_node = queue[0]
                
                    node.next = next_node
                #     node = node.next
            # node.next = None

            
        
        return root

