# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
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
        
        # End Carry Has Two Cases
        
        # Case 1 : If list are not of equal length
        # We need to add the remaining as well as Carry if present
        
        if l1 is None or l2 is None:
            
            if l1 is None:
                prev.next = self.addList(l2, carry)
                
            else:
                # Handle Carry inside  AddList
                prev.next = self.addList(l1,carry)
                
         # Case 2 : if lists were equal length, handle carry
        else:
           

            if carry > 0:
                prev.next = ListNode(carry)
        return dummy.next

  
       

        
        

        
