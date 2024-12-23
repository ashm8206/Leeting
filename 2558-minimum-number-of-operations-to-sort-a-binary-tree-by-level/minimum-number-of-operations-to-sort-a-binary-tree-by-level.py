# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        
        q = deque()
        q.append(root)
        total_swaps = 0
        while q:
            n = len(q)
            level_nodes = []
            for _ in range(n):
                root = q.popleft()
                val = root.val
                level_nodes.append(val)

                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)

            total_swaps += self.get_min_swaps(level_nodes)
        return total_swaps

    def get_min_swaps(self, original):

        target = sorted(original)

        pos = {val: idx for idx, val in enumerate(original)}
        swaps = 0

        n = len(original)

        for i in range(n):
            if original[i]!= target[i]:
                swaps +=1

                actual_pos = pos[target[i]] # pos where target is
                pos[original[i]] = actual_pos

                original[actual_pos] = original[i] # update the original array
        
        return swaps





        


        