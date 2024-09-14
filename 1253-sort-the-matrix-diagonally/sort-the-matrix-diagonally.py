from collections import defaultdict
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        nRows = len(mat)
        nCols = len(mat[0])

        def counting_sort(ls):

            freq = [ 0 for i in range(101)]
            result = [0] * len(ls)

            for num in ls:
                freq[num]+=1
            
            for i in range(1,101): # len freq
                freq[i] += freq[i-1]
            
            for num in ls:
                idx = freq[num] # getCorrect idx
                result[idx-1] = num 
                # idx - 1 # Index has to -1 as you initialized maxNum+1
                freq[num]-=1

            return result
            
    
        # Method I
        diag_map = defaultdict(list)

        for i in range(nRows):
            for j in range(nCols):
                diag_map[i-j].append(mat[i][j])
        
        for diag_key, diag_val in diag_map.items():
            diag_map[diag_key] = counting_sort(diag_val)
        
        for i in range(nRows):
            for j in range(nCols):
                mat[i][j] = diag_map[i-j].pop(0)
        
        return mat 

        
    # Method II - Counting Sort
    #     r = 0
    #     for c in range(nCols):
    #         self.sort_diagonal_starting_at(mat, r, c)
            
    #     c = 0
    #     for r in range(1, nRows):
    #         self.sort_diagonal_starting_at(mat, r, c)
            
    #     return mat
        
    # def sort_diagonal_starting_at(self, mat, start_r, start_c):
    #     nRows = len(mat)
    #     nCols = len(mat[0])
        
    #     freq = [0 for _ in range(100+1)]
        
    #     r = start_r
    #     c = start_c
    #     while r < nRows and c < nCols:
    #         freq[mat[r][c]] += 1 # number idx +=1
            
    #         r += 1 # get numbers on the diagonal
    #         c += 1
        
    #     r = start_r
    #     c = start_c
    #     for i in range(len(freq)):
    #         for j in range(freq[i]): # this ensures all numbers are processed
    #             mat[r][c] = i # place the number
                
    #             r += 1 # place numbers on the diagonal location
    #             c += 1