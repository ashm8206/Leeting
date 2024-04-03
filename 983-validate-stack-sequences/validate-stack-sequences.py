class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []

        j = 0

        n = len(pushed)
        m = len(popped)

        for i in range(n):
            
            stack.append(pushed[i])

            while stack  and stack[-1]==popped[j]:
                j+=1
                stack.pop()
            
            

            
        return  j == m
