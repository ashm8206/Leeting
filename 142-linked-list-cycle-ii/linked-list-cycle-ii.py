# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        hasCycleBool, fast = self.hasCycle(head)
        if not hasCycleBool:
            return None

        # reset both of them
        slow = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return fast

    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True, fast
        return False, None