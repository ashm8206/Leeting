class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

         # the problem is not merely asking you to dedeup the string
         # it is also asking you to return smallest lexographic string
         # with all unique charcaters, so skipping

         # What (2 things)
        #  1. Remove Duplicate letter
        #      retain first copy, if already in result, skip

        #  2. Return Lexographically smallest
        #     while stack[-1] > c  pop it only if it will be seen again 
                    #  i < last_Occurence[stack[-1]]
        #    if it cant be seen again, or seen first time 
        #    add to stack
        #      in case stack[-1] cant be seen again, new string append 
        #      will break the monotonically increasing stack,
        #      but thats okay, as we must not SKIP any elements

        

        stack = []

        last_occurence = {c:i for i, c in enumerate(s)}

        for i, c in enumerate(s):

            if c in stack:
                continue

            while stack and stack[-1] >= c and  i < last_occurence[stack[-1]]:
                # we got a b and stack contains [acd]
                # technically we should remove "d" but only if  i < lastOccurence[topOfStack]
                # we must
                #  i: construct a lexogrpahically smallest
                #     pop all greater than current character  only if we are guaranteed to see the charcater again
                stack.pop()
            
            stack.append(c)
         

        return "".join(stack)


