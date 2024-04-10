class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        cols = len(max(words, key=lambda x:len(x)))
        rows = len(words)

        row_wise = [['']*cols for i in range(rows)]

        for i, word in enumerate(words):
            for j, char in enumerate(word):

                row_wise[i][j]=char
        #
        ans = True
        for i in range(rows):
            
            for j in range(cols):
    
                if j >= rows or i>=cols or row_wise[i][j]!=row_wise[j][i]:
                    return False
                
                ans &=True
            
            # if ans==True:
            #     print(row_wise[i])
            #     return True
        return ans

        