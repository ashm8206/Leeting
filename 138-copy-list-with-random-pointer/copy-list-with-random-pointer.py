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

        # Recursive
        # self.visited = {}

        # def helper(node):

        #     if not node:
        #         return None
            
        #     if node in self.visited:
        #         return self.visited[node]
            
        #     new_node = Node(node.val, None, None)

        #     self.visited[node] = new_node

        #     new_node.next = helper(node.next) if node.next else None
        #     new_node.random = helper(node.random) if node.random else None

        #     # Postorder will create recursion exceeded. as Random could pt to a node already seen.

        #     return new_node
        # return helper(head)


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

        if not head:
            return None
        
        curr = head

        # A-->A'-->B-->B'
        while curr:
            new_node = Node(curr.val, None, None)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        
        # Set Random ptrs

        curr = head
        while curr and curr.next:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        ptrA = head
        ptrB = head.next
        dummy = Node(-1)
        dummy.next = head.next

        while ptrA and ptrB:
            ptrA.next = ptrB.next
            ptrB.next = ptrB.next.next if ptrB.next else None

            ptrA = ptrB.next
            ptrB = ptrB.next
        # We cant combine the two Random+unweaving cuz we need next ptrs intact
        return dummy.next


    
    


