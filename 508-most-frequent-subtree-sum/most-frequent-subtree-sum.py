# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        hmap = defaultdict(int)
        freqMap = defaultdict(list)
        maxFreq = 0

        def helper(root):
            
            nonlocal maxFreq
            if not root:
                return 0

            leftSum = helper(root.left)
            rightSum = helper(root.right)

            curr_sum = leftSum + rightSum + root.val
            hmap[curr_sum] += 1

            freqMap[hmap[curr_sum]].append(curr_sum)
            maxFreq = max(hmap[curr_sum], maxFreq)

            return curr_sum

        helper(root)
        return freqMap[maxFreq]
        


