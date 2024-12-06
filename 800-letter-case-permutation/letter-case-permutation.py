class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n= len(s)
        def backtrack(idx,slate):
            if len(slate)==n:
                # print(slate)
                output.append("".join(slate[:]))
                return
        
            
            if s[idx].isalpha(): # Alphabet
                slate.append(s[idx].upper())
                backtrack(idx+1,slate)
                slate.pop()

                slate.append(s[idx].lower())
                backtrack(idx+1,slate)
                slate.pop()

            else:
                slate.append(s[idx])
                backtrack(idx+1,slate)
                slate.pop()
            # for i in range(first, n):
            #     if slate[first].isalpha():
            #         changed_case = slate[first].lower() if slate[first].isupper() else slate[first].upper()
            #         slate = slate[:first]+changed_case+slate[first+1:]
            #         #print(changed_case)
            #     backtrack(first + 1, slate)
            #     slate = slate[:]

                
        output =[]
        #backtrack()
        backtrack(0, [])
        return output
        #print(len(output))