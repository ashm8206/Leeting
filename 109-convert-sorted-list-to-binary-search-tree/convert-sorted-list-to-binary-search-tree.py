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
    # def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        

        # def findMiddle(root):
        #     if root is None or root.next is None:
        #         return root

        #     slow = head
        #     fast = head
        #     prev = None
        #     while fast and fast.next:
        #         prev = slow
        #         slow = slow.next
        #         fast = fast.next.next

        #     if prev:
        #         #unlink lift
        #         prev.next = None
            
        #     return slow

          
  

        
        # if head is None:  # or head.next is None: return head of Type TREENODE
        #     return None

        # if head.next is None:
        #     return TreeNode(head.val)
        
   
        # mid =  findMiddle(head)
        # node = TreeNode(mid.val)

        # node.left = self.sortedListToBST(head)
        # node.right = self.sortedListToBST(mid.next)
        # return node

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
            
            # recurse left
            left = convert(l, mid - 1)

            # place
            node = TreeNode(head.val)
            node.left = left

            # head will pt always need to pt to next node to place
            # hence made head Non-local
            head = head.next

            # Recurse on right
            node.right = convert(mid + 1, r)
            return node

        return convert(0, size - 1)
        #  TC: O(N)
        #  Spac: Log(N)

        
        
        


            
