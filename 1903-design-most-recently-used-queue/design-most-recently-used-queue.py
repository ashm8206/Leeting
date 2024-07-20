class Node(object):

    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class MRUQueue(object):

    def __init__(self, n):
        """
        :type n: int
        """

        self.dummyStart = Node(-1)

        #Atleast 1
        curr = Node(1)
        self.dummyStart.next = curr
        curr.prev = self.dummyStart
      
        for i in range(2, n+1):
            new_node = Node(i)
            curr.next = new_node
            new_node.prev = curr
            curr = curr.next
           
        self.dummyEnd = Node(-1)
        curr.next = self.dummyEnd
        self.dummyEnd.prev = curr
        
    

    def fetch(self, k):
        """
        :type k: int
        :rtype: int
        """

        curr = self.dummyStart.next
        k = k - 1
        print("k : {0}".format(k))
       
        # Get 
        while k:
            curr = curr.next  # 1
            k-=1
        print("--")
        # Detach
        next_node = curr.next
        prev_node = curr.prev

        curr.next = None
        curr.prev = None

        prev_node.next = next_node
        next_node.prev = prev_node

        # Append to end
        lastNode = self.dummyEnd.prev
        
        lastNode.next = curr  # curr is the target Node
        curr.prev = lastNode
        curr.next = self.dummyEnd
        self.dummyEnd.prev = curr

        # print(lastNode.val, lastNode.next.val, curr.next.val, curr.prev.val, self.dummyEnd.prev.val)

        return curr.val

        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)