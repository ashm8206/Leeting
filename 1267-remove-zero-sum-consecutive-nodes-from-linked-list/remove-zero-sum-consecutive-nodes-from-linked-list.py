# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1,2,3,

        arr = []
        

        def getArray(head,arr):
            curr = head
            while curr:
                arr.append(curr.val)
                curr= curr.next
            
            return arr
        
        def subArray(arr):
            n = len(arr)
            for i in range(n):
                curr_sum = arr[i]
                for j in range(i+1, n):
                    curr_sum+=arr[j]
                    if curr_sum == 0:
                        for erase in range(i,j+1):
                            arr[erase]= 0

            return [ val for val in arr if val!=0]

        def createList(arr):
            dummy = ListNode(-1)
            curr = dummy
            for val in arr:
                if dummy.next is None:
                    dummy.next = ListNode(val)
                else:
                    curr.next = ListNode(val)
                curr = curr.next
            return dummy.next
                

        
        arr = getArray(head, [])

        non_zero_arr = subArray(arr)

        new_head = createList(non_zero_arr)

        return new_head