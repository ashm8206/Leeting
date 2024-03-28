class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        mapping ={")":"(","}":"{","]":"["}
        
        for bracket in s:
            if bracket not in mapping:
                stack.append(bracket)
            elif stack and stack[-1] == mapping[bracket]:
                # 1 and 1
                # match found
                stack.pop()
            else:
                # closing bracket and stack empty (no opening bracket)
                # closing bracket and stack[-1] != mapping[bracket]
                return False
        return len(stack)==0

        
    
    # if all stack is popped when pairs come, then it will be empty. We need to account for uncompleted pairs
    
    #1 starts with end "]" stack empty and ending bracket encoutered
    #2 "[" starts with open no closing . stack not empty at the end of for loop
    #3 "(]" popped opening bracket does not match closed bracket
    #4 "{[]}" our desered result