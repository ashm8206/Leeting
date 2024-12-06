class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #  Method I
        # n= len(s)
        # def backtrack(idx,slate):
        #     if len(slate)==n:
        #         # print(slate)
        #         output.append("".join(slate[:]))
        #         return
        
            
        #     if s[idx].isalpha(): # Alphabet
        #         slate.append(s[idx].upper())
        #         backtrack(idx+1,slate)
        #         slate.pop()

        #         slate.append(s[idx].lower())
        #         backtrack(idx+1,slate)
        #         slate.pop()

        #     else:
        #         slate.append(s[idx])
        #         backtrack(idx+1,slate)
        #         slate.pop()
        #     # for i in range(first, n):
        #     #     if slate[first].isalpha():
        #     #         changed_case = slate[first].lower() if slate[first].isupper() else slate[first].upper()
        #     #         slate = slate[:first]+changed_case+slate[first+1:]
        #     #         #print(changed_case)
        #     #     backtrack(first + 1, slate)
        #     #     slate = slate[:]

                
        # output =[]
        # #backtrack()
        # backtrack(0, [])
        # return output
        # #print(len(output))

        #Method II

     
        result = []
        # Convert string S into a list to easily mutate characters
        S = list(s)

        # Count the number of letters
        B = sum(c.isalpha() for c in S)
        
        # Generate all possible bitmasks (2^B possible combinations)
        for mask in range(2 ** B):
            temp = S[:]  # Copy the original list
            letter_idx = 0  # To track the index of letters in S
            for i in range(len(S)):
                if S[i].isalpha():  # If the character is a letter
                    # Use the bitmask to decide whether to change case
                    if (mask >> letter_idx) & 1:
                        temp[i] = temp[i].upper()  # Change to uppercase
                    else:
                        temp[i] = temp[i].lower()  # Change to lowercase
                    letter_idx += 1
            # Add the generated string to the result
            result.append(''.join(temp))
        
        return result
