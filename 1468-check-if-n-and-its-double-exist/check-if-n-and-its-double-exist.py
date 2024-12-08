class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        hmap = {num:j for j, num in enumerate(arr)}

        for i, num in enumerate(arr):
  
            if num*2 in hmap:
                if i==hmap[num*2]:
                    continue
                else:
                    return True
        return False   
