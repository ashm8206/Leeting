# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Recursive
        # if list1 is None:
        #     return list2
        # elif list2 is None:
        #     return list1
        # elif list1.val <= list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2

        # Iterative # Method I

        curr = new_head = ListNode(0)
        l1 = list1
        l2 = list2
        while l1 or l2:
            # when do we add L1 ?
            if (l2 is None) or (l1 and l1.val <= l2.val):
                curr.next = l1
                l1 = l1.next
            else:
                # l2 is Not None and  l2 >= l1
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        return new_head.next

        #  Method II

    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next