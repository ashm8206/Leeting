"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """

        res = []
        def ser(root):
            if not root:
                return ""
            res.append(str(root.val))
            res.append(str(len(root.children)))
            for child in root.children:
                ser(child)
            
        ser(root)
        print(",".join(res))
        return ",".join(res)
        

        
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if len(data) == 0:
            return None
        res = data.split(",")
        q = deque()
        for i in range(len(res)):
            q.append(res[i])

        def deser(nodes):
            if len(nodes) > 0:
                val = nodes.popleft()
                totalKids = int(nodes.popleft())
                root = Node(int(val), [])
                for i in range(totalKids):
                    root.children.append(deser(nodes))
                return root
            else:
                return None
        return deser(q)



        

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))