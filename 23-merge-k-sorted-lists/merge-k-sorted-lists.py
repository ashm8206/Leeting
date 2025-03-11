# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        pq =[]
        k = len(lists)
        for i in range(k): 
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i))
                lists[i] = lists[i].next
        
        prevHead = ListNode(-1)
        curr = prevHead
        while pq:
            minVal, idx = heapq.heappop(pq)

            curr.next = ListNode(minVal)
            curr = curr.next
            
            if lists[idx]:
                heapq.heappush(pq, (lists[idx].val, idx))
                lists[idx] = lists[idx].next

        return prevHead.next


        
       
        # pq = []
        # curr = head = ListNode()
        # prev = ListNode(-int(10**5))
        
        # k = len(lists)
        # if k < 1:
        #     return None

        # for i in range(k):
        #     if lists[i]:
        #         # value and index of the list
        #         pq.append((lists[i].val, i))
        #         lists[i] = lists[i].next
        
   
    
        # heapq.heapify(pq)
        # while pq:
        #     next_num, idx = heapq.heappop(pq)
        #     if lists[idx]:
        #         heapq.heappush(pq,(lists[idx].val, idx))
        #         lists[idx] = lists[idx].next
            
            
        #     curr = ListNode(next_num)
        #     prev.next = curr

        #     if prev.val == -10**5 and prev.next:
        #         head.next = prev.next
            
        #     prev = curr


        # if head.next is None:
        #     return None
        # else:
        #     return head.next
            
      