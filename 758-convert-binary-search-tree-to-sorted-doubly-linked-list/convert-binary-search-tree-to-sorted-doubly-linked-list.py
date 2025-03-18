"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

            def helper(curr):
                nonlocal H, prev
                if not curr:
                    return
                
                helper(curr.left)

                if prev:
                    prev.right = curr
                    curr.left = prev
                else:
                    H = curr # this is what we return

                prev = curr

                helper(curr.right) # Like saying curr.next


            if not root:
                return root
            H, prev = None, None
            # H --> way deeep down, so we need a ref for it qst time we see it
            # T --> prev
            # root --> currr

            helper(root)

            # prev pts to
            H.left = prev 
            prev.right = H
            # circular doubly linkedlist

            return H




        
        # if not root:
        #     return None
        
        # stack = []
        # # We must Re-use Left and Right Ptrs
        # dummy = Node(-1)
        # #For Foubly linkedlist we need 2 References [Prev, curr.next]
        # prev = dummy
        # # For smallest element in BST prev is dummy

        # # We do an iterative inorder traversal
        # curr = root
        # while stack or curr:

        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
            
        #     curr = stack.pop()
        #     # Print/ process
        #     prev.right = curr
        #     curr.left = prev
        #     prev = curr
        #     curr = curr.right

        # # Make circular doubly
        # dummy.right.left = prev  # prev is no is the last node in DLL
        # prev.right = dummy.right
        # return dummy.right