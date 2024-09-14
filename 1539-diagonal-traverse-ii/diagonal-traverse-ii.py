class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # Addition R+C: Bottom L  to Top R (distinct Keys)
        # 0,1 , 1,0 
        # 0,2,  1,1, 2,0
        # 2,1  1,2
        # 2,2
        # It is sequential the keys, so we can initial curr accordingly

        # Subtraction R-C: Top L  to Bottom R (distinct Keys)
        # 1,0 , 2,1:  1
        # 0,1 , 1,2 : -1

        n = len(nums)
        hmap = defaultdict(list)
        for i in range(n):
        # for i in range(n-1, -1, -1): 
            # start processing from Bottom Right
            for j in range(len(nums[i])):
                hmap[i+j].append(nums[i][j])
        
        
        res = []
        curr = 0 # index of the keys
        
        while curr in hmap.keys():
            # res.extend(hmap[curr][::-1]) # extra complexity if we process from top left
            # Instead we process above while loop from Bottom right
            # res.extend(hmap[curr])
            res.extend(hmap[curr][::-1])
            curr+=1
        return res
        





        
        
        