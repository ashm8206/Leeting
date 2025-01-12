# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def predecessor(self, root: TreeNode) -> TreeNode:
        root = root.left
        while root.right:
            root = root.right
        return root.val
    
    def successor(self, root: TreeNode) -> TreeNode:
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        # print(root.val, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left =self.deleteNode(root.left, key)
        else:
            # We found the node
            # this node leaf node
            if root.left is None and root.right is None:
                root = None

            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)

            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            
        return root
            

            # #     # root.right root ahs right 
            # 1. root has left child
            # 2. root has right child
            # 3. root has l+r child
            # # next right / l+r greater  to be added 
            # # delete the successor from tree

            # add prdeccessor 
            # delete predecesor

