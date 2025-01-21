# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def ser(root):
            if not root:
                res.append("None,")
                return
            res.append(str(root.val)+ ",")
            ser(root.left)
            ser(root.right)
        ser(root)
        # print(res)
        return "".join(res)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deser(nodes):
            if not nodes:
                return None
            if nodes and nodes[0] == 'None':
                nodes.pop(0)
                return None
            
            root = TreeNode(int(nodes[0]))
            nodes.pop(0)
            root.left = deser(nodes)
            root.right = deser(nodes)
            return root
        

        nodes = data.split(",")
        # print(data)
        return deser(nodes)



    # def serialize(self, root):
    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """
        
    #     if not root:
    #         return ''

    #     res = []
    #     queue = collections.deque()
    #     queue.append(root)

    #     while queue:
    #         node = queue.popleft()
    #         if not node:
    #             res.append('None')
    #         else:
    #             res.append(str(node.val))
    #             queue.append(node.left)
    #             queue.append(node.right)
            
    #     while res[-1]=='None':
    #         res.pop()
    #     return ','.join(res)

    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     if not data:
    #         return None

    #     ls = data.split(',')
    #     root = ls.pop(0)
        
    #     new_root = TreeNode(int(root))
        
    #     queue = collections.deque()
    #     queue.append(new_root)
    

    #     while queue:
    #         node = queue.popleft()
        
            
    #         if len(ls) > 0:
    #             if ls[0]!= 'None':
    #                 node.left = TreeNode(int(ls.pop(0))) 
    #                 queue.append(node.left)
    #             else:
    #                 ls.pop(0)
    #                 node.left = None

    #         if len(ls) > 0:
    #             if ls[0]!= 'None':
    #                 node.right = TreeNode(int(ls.pop(0))) 
    #                 queue.append(node.right)
    #             else:
    #                 ls.pop(0)
    #                 node.right = None

    #         # print(ls, queue)
    #     return new_root


        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))