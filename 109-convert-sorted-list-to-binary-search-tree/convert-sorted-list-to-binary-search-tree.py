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
        

        def helper(head, tail):
            if head == tail:
                return None

            
            slow, fast = head, head

      
            while fast!= tail and fast.next!=tail:
                slow = slow.next
                fast = fast.next.next
            

            root = TreeNode(slow.val) # slow is at mid
            root.left = helper(head, slow)
            root.right = helper(slow.next, tail)

            return root
        
        if root is None:
            return None
    
        return helper(head, None)
         # # Taking the Middle most ensure balanced Property
        # #TC:  ONLOGN : 
        # #SC:  O(LogN)
          
  

    
    def findSize(self, head: ListNode) -> int:
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
        return c

    def sortedListToBST(self, head: ListNode) -> TreeNode:

        # Get the size of the linked list first
        size = self.findSize(head)

        # Recursively form a BST out of linked list from l --> r
        def convert(l: int, r: int) -> TreeNode:
            nonlocal head

            # Invalid case
            if l > r:
                return None
        
            mid = (l + r) // 2
            
            # you have to do INORDER cuz you cant access the MID like that!
            # recurse left
            first = convert(l, mid - 1)

            # place
            node = TreeNode(head.val)
            node.left = first

            # head will pt always need to pt to next node to place
            # hence made head Non-local
            head = head.next

            # Recurse on right
            node.right = convert(mid + 1, r)
            return node

        return convert(0, size - 1)
        #  TC: O(N)
        #  Spac: Log(N)

        
        
        


            
