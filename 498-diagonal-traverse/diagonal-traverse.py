from collections import OrderedDict,defaultdict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        # hmap = OrderedDict()
        
        # for i in range(m):
        #     for j in range(n):
        #         key = i+j
        #         if key not in hmap:
        #             hmap[key] = []
                
        #         hmap[key].append(mat[i][j])
    
        # res = []
        # flip = 1
        # for key, val in hmap.items():
        #     if flip:
        #         res.extend(val[::-1])
        #     else:
        #         res.extend(val)
        #     flip^=1

        # return res
        # O(N*M)
        # O(N*M)

        # Can use Regular Dictionaries and Order is preserved   
        # https://docs.python.org/3.7/library/stdtypes.html#dict.values

        # Dictionaries not expected to be in Order 
        # for key in range (0, (rows-1) * (cols-1)): 
        #        0, 1,2,3,4

    
        
        dir = 1
        row, col = 0, 0
        res = []
        for _ in range(n*m):
            res.append(mat[row][col])
                
            if dir == 1: # up - right
                if col == n -1:
                    row+=1
                    dir = -1
                elif row==0:
                    col+=1
                    dir = -1
                else:
                    row -=1 
                    col += 1
            
            else: # down - right
                if row == m-1: # last row
                    col+=1
                    dir = 1

                elif col==0:
                    row+=1
                    dir = 1
                else:
                    row+=1
                    col-=1
        return res

            


