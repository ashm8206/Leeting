# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def findMiddle(root):
            if root is None or root.next is None:
                return None, root, None
                # return root

            left = head
            slow = head
            fast = head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            if prev:
                prev.next = None
            
            # unlink slow   
            right = slow.next
            slow.next = None
            
            return left, slow, right
            # return slow
  

        if head is None:
            return head
        
        left, mid, right = findMiddle(head)
        node = TreeNode(mid.val)
        node.left = self.sortedListToBST(left)
        node.right = self.sortedListToBST(right)
        return node
        
        # mid = findMiddle(head)
        # node = TreeNode(mid.val)

        # if head == mid:
        #     return node
        
        # node.left = self.sortedListToBST(head)
        # node.right = self.sortedListToBST(mid.next)
        # return node
            


            
