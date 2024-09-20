"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':


        self.visited = {}

        def helper(node):

            if not node:
                return None
            
            if node in self.visited:
                return self.visited[node]
            
            new_node = Node(node.val, None, None)

            self.visited[node] = new_node

            new_node.next = helper(node.next) if node.next else None
            new_node.random = helper(node.random) if node.random else None

            return new_node
        return helper(head)


        #  Iterative + O(N)

        # dummy = ListNode(-1)
        # dummy.next = head
        # curr = head
        # hmap = {}
        # Create Node 1st

        # while curr: 
        #     _curr = Node(curr.val)
        #     hmap[curr] = _curr
        #     curr = curr.next

        
        
        # LinkNodes
        # curr = head
        # while curr:

        #     _curr = hmap[curr]
        #     _curr.next = hmap[curr.next] if curr.next is not None else None
        #     _curr.random = hmap[curr.random] if curr.random is not None else None
        #     curr = curr.next

        # return hmap.get(head,None)

        # Iterative O(1) Space

        # if not head:
        #     return head

        # # Weave
        # curr = head
        # while curr:
        #     nextNode = curr.next
        #     newNode = Node(curr.val)
        #     curr.next = newNode
        #     newNode.next = nextNode
        #     # print(curr.val,curr.next.val)
        #     curr = nextNode

        # # Random ptr Assignment
        # ptr = head

        # while ptr and ptr.next:
        #     if ptr.random:
        #         ptr.next.random = ptr.random.next 
        #     ptr = ptr.next.next

        # ptrA = head
        # ptrB = head.next

        # newHead = ptrB

        # # A - A' - B - B' - C - C' 
        # # pA
        # #     pB

        # # Unweave
        # while ptrA :
        #     ptrA.next = ptrB.next if ptrB else None
        #     ptrB.next = ptrB.next.next if ptrB.next else None

        #     ptrA = ptrA.next
        #     ptrB = ptrB.next
        # # We cant combine the two Random+unweaving cuz we need next ptrs intact
        # return newHead

    
    


