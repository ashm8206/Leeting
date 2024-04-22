# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        current = root
        queue.append(current)

        '''
        ans = root.val

        while queue:
            size = len(queue)

            for i in range(size):
                current = queue.popleft()

                if i == 0:
                    ans = current.val

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

        return ans

        '''

        while queue:

            node = queue.popleft()
            
            if node.right:
                queue.append(node.right)
            
            if node.left:
                queue.append(node.left)
        
        return node.val