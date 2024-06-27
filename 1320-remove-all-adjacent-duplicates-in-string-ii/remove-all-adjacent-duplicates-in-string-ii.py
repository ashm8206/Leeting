class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        # # Method I - Two Stacks, You can also use a 2D stack
        # stack = []
        # counterStack = []

        # n = len(s)

        # for i in range(n):
            
        #     if not stack or s[i]!=stack[-1]:
        #         counterStack.append(1)

        #     elif s[i]==stack[-1]:
        #         counterStack[-1]+=1
            
        #     stack.append(s[i])
        #     # print(counterStack,stack)
            
        #     if counterStack[-1]==k:
        #         while counterStack[-1] and stack:
        #             stack.pop()
        #             counterStack[-1]-=1
        #         counterStack.pop()
        #         # print(counterStack,stack)
            
        # return "".join(stack)
        
        # # Two pointer (Imteresting Use-case for two pointer)

        # slow = 0
        # counterStack = []
        # s = list(s)

        # for fast, c in enumerate(s):
        #     # place char ar next slow position
        #     s[slow] = c
            
        #     if slow == 0 or s[slow]!=s[slow-1]:
        #         counterStack.append(1)
        #     else:
        #         counterStack[-1]+=1
        #         if counterStack[-1]==k:
        #             slow-= k
        #             counterStack.pop()
        #             # remove k dups
        #             # now slow is poiting to next valid position
        #     slow+=1
        #     # in each iteration we ince slow+1
        # return "".join(s[:slow])

        stack = []
        n = len(s)

        for i in range(n):
            
            if not stack or (stack[-1][0]!=s[i]):
                stack.append([s[i],1]) #char, cnt nested list
            else:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop() # pop this entry, it meets dup criterion
            
        
        return "".join(char*count for char, count in stack)
       
            

                


        