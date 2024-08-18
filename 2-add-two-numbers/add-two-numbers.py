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
            
        
        if l1 is None or l2 is None:
            
            if l1 is None:
                prev.next = self.addList(l2, carry)
                
            else:
                
                prev.next = self.addList(l1,carry)
            #carry = 0 # handled inside so make it 0
        else:
            # if lists were equal length, handle carry here too

            if carry > 0:
                prev.next = ListNode(carry)
        return dummy.next

        '''
            In each else, it returns a new List of Unknown size
            # prev.next --> [ node1 --> node2 --> node3]

            We can't simply, prev.next this, as we don't know 
            How many # times to keep, prev = prev.next

        '''

        '''
             So we  handle carry twice / Two cases
             1. Once for Len(l1) < Len(l2), incase there is carry
             2. Once incase L1==L2  and there is Carry

             Since we handle 2 by Default, we must set carry step 1 to 0 
             Else we will end up adding carry incorrectly
            #  We get Prev-->[carry]
            # When we expect  prev.next --> [ node1 --> node2 --> node3[carry].
            We actually, end up undoing our previously done work. 
            As we not prev.next  in IF statement, as len addList returned is unknown
        ''' 
            
       

        
        

        
