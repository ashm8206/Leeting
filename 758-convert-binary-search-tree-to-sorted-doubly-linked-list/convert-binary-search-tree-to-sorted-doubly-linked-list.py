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
        

        if not root:
            return root

        def helper(curr, first, prev):
            if not curr:
                return first, prev
            
            # 1. Process left subtree
            # Passes current tracking nodes, returns updated ones from left side
            first, prev = helper(curr.left, first, prev)

            # 2. Process current node
            if not prev:
                # This is the leftmost node, the head of our list
                first = curr
            else:
                # Link current node with the previous node
                curr.left = prev
                prev.right = curr
            
            # Update prev to be the current node for the next step
            prev = curr

            # 3. Process right subtree
            # Returns the final state of first and prev for this entire branch
            return helper(curr.right, first, prev)

        # Initial call with first and prev as None
        firstNode, lastNode = helper(root, None, None)

        # 4. Close the circular loop
        firstNode.left = lastNode
        lastNode.right = firstNode

        return firstNode







        # firstNode = None
        # prev = None

        # def helper(curr):
        
        #     nonlocal firstNode, prev

        #     if not curr:
        #         return curr
            
        #     helper(curr.left) # set he first node

        #     if not prev:
        #         firstNode = curr
        #     else:
        #         curr.left = prev
        #         prev.right = curr # curr.right will be set in the nex iteration

        #     prev = curr
        #     helper(curr.right)
    
        # if not root:
        #     return root
        
        # helper(root)

        # firstNode.left = prev
        # prev.right = firstNode

        # return firstNode



          



        
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