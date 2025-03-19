# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        # # Iterative:
        i = 0
        n = len(s)
        stack = []
        while i < n:
            # process digits
            if s[i]=="-" or s[i].isdigit():
                curr = s[i]
                i+=1

                while i < n and s[i].isdigit():
                    curr += s[i]
                    i += 1
                 

                node = TreeNode(int(curr))
                
                if stack:
                    parent = stack[-1]
                    if parent.left is None:
                        parent.left = node
                    else:
                        parent.right = node

                stack.append(node)
                # print(stack)

            elif s[i]=="(":
                i+=1
            else:
                i+=1
                stack.pop() # pop this level
        return stack[0] if stack  else None
        



        # Recursive
        # ix = s.find('(')
        # if ix < 0:
        #     return TreeNode(int(s)) if s else None
            
        # bal = 0
        # for jx, u in enumerate(s):
        #     if u == '(': bal += 1
        #     if u == ')': bal -= 1
        #     if jx > ix and bal == 0:
        #         break

        openIdx = s.find("(")
        if openIdx < 0:
            return TreeNode(int(s)) if s else None
        
        bal = 0
        closeIdx = 0
        for i in range(len(s)):
            if s[i]=="(": bal+=1
            if s[i]==")": bal-=1
            if bal==0 and i > openIdx and s[i]==")":
                closeIdx = i
                break

        root = TreeNode(int(s[:openIdx]))
        root.left = self.str2tree(s[openIdx+1:closeIdx]) # don't include "outmost )"
        root.right = self.str2tree(s[closeIdx+2:-1]) # last but one 
        return root