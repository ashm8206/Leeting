# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rest

    
    def addList(self, remainList, carry) -> tuple[ListNode(int), int]: 

        dummy = ListNode(-1)
        prev = dummy
        while remainList:
            add = remainList.val + carry
            carry, result = divmod(add, 10)
            prev.next = ListNode(result)
            prev = prev.next
            remainList = remainList.next
        if carry > 0:
            prev.next = ListNode(carry)
        return dummy.next


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)


        dummy = ListNode(-1)
        prev = dummy
        carry = 0
        while l1 and l2:
            add = l1.val + l2.val + carry
            carry, result = divmod(add, 10)
            prev.next = ListNode(result)
            prev = prev.next
            l1 = l1.next
            l2 = l2.next
        
        
        #If list are not of equal length
        # We need to add the remaining as well as Carry if present
        
    
            
        if l1 is None:
            prev.next = self.addList(l2, carry)
            # Handle Carry inside  AddList
        else:
            
            prev.next = self.addList(l1,carry)

        return self.reverseList(dummy.next)

  