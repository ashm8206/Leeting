# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode(0)
        dummyNode.next = head

        # Flaw 2: What if head changes?
        # Initialzie curr @ dummy

        curr = dummyNode

        hmap = {}
        prefix_sum = 0

        while curr:
            prefix_sum += curr.val

            if prefix_sum in hmap:
                # We keep this start node.
                # start+1 .. curr will be removed
                #  1. Removed From Hmap
                #  2. Removed from Linkedlist 
                startNode = hmap[prefix_sum]

                sub_curr = startNode.next

                # delete startNode --> curr.node - 1  values from hmap
                # we only traverse till curr - 1, as we never added curr in hmap
                # prefix @ Curr = prefix @ StartNode
                # It wil give key error or worse, delete prefix @startNode, which is valid
                
                # Flawed Approach 1 : what if its Single node to delete
            
                # while sub_curr and sub_curr.next!=curr:
                #     sub_prefix_sum += sub_curr.val

                #     del hmap[sub_prefix_sum]
                #     sub_curr = sub_curr.next

                startNode = hmap[prefix_sum]
                curr = startNode.next
                
                p = prefix_sum + curr.val
                # del startNode.next --> curr -1 
                # at curr = p = prefix_sum
                while p != prefix_sum:
                    del hmap[p]
                    curr = curr.next
                    p += curr.val
           
                startNode.next = curr.next

            else:
                hmap[prefix_sum] = curr 
            
            curr = curr.next

        return dummyNode.next