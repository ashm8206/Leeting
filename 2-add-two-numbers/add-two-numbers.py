# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        curr = dummy
        carry = 0
        

        while l1 or l2 or carry:
            
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            total =  digit1 + digit2 + carry
            carry, total = divmod(total, 10)
            
            
            new_node = ListNode(total)
            curr.next = new_node
            curr = curr.next

            # if l1:
            #     l1 = l1.next
            # if l2:
            #     l2 = l2.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
       # def addList(self, remainList, carry) -> tuple[ListNode(int), int]:
    #     dummy = ListNode(-1)
    #     prev = dummy
    #     while remainList:
    #         add = remainList.val + carry
    #         carry, result = divmod(add, 10)
    #         prev.next = ListNode(result)
    #         prev = prev.next
    #         remainList = remainList.next
    #     if carry > 0:
    #         prev.next = ListNode(carry)
    #     return dummy.next


    #     dummy = ListNode(-1)
    #     prev = dummy
    #     carry = 0
    #     while l1 and l2:
    #         add = l1.val + l2.val + carry
    #         carry, result = divmod(add, 10)
    #         prev.next = ListNode(result)
    #         prev = prev.next
    #         l1 = l1.next
    #         l2 = l2.next
        
        
    #     #If list are not of equal length
    #     # We need to add the remaining as well as Carry if present
        
    
            
    #     if l1 is None:
    #         prev.next = self.addList(l2, carry)
    #         # Handle Carry inside  AddList
    #     else:
            
    #         prev.next = self.addList(l1,carry)

    #     return dummy.next

  
       

        
        

        
