# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # queue = deque([root])
        # heap = []

        # while queue:
        #     curr = queue.popleft()
            
        #     if len(heap) < k:
        #         heappush(heap, -curr.val)
        #     elif heap[0] <= -curr.val:
        #         heappop(heap)
        #         heappush(heap, -curr.val)

        #     if curr.left:
        #         queue.append(curr.left)

        #     if curr.right:
        #         queue.append(curr.right)

        # if heap:
        #     return heap[0] * -1
        # return -1

        
        if not root:
            return -1

        curr = root
        stack = [curr]

        while True:

            if curr:
                stack.append(curr)
                curr = curr.left
            
            elif stack:
                curr = stack.pop()
                k-=1 
                if k==0:
                    return curr.val
                
            
                curr = curr.right
            else:
                break


        
        


        # -3 - 2, -1