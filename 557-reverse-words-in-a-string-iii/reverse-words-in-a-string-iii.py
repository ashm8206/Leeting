class Solution:
    def reverseWords(self, s: str) -> str:
        
        """
        s.split(" ") O(M) Space
        Read it Reverse it O(N)
        JOIN
        
        """
        """
        n * n means is every ith char will traverse all n char. But here outer loop iterate 4 times means inner loop also iterate 4times after inner loop done. outer loop start iterate 8 times means inner loop also do same amount of iteration. so outer loop == inner loop so tc is O(n+n)
        
        """

        # word_list = s.split(" ")
        # res =[] # array of string

        # for w in word_list:
        #     res.append(w[::-1])
        # # print(res)

        # return " ".join(res)

        

        stack = s.split(" ")

        for k, word in enumerate(stack):
            i = 0
            j = len(word)-1
            ls = list(word)
            while i < j:
                ls[i], ls[j] = ls[j], ls[i]
                i+=1
                j-=1
            stack[k] = "".join(ls)
        return " ".join(stack)

        # start_idx = 0
        # end_idx=0
        # res = []
        # for i, char in enumerate(s):

        #     if char.isspace():
        #         ## Below can be two pointer!
        #         res.append(s[start_idx:end_idx][::-1])
        #         start_idx = i+1
        #         end_idx = start_idx

        #     elif end_idx == len(s)-1:
        #         res.append(s[start_idx:end_idx+1][::-1])
        #     else:
        #         end_idx+=1
        # return " ".join(res)


