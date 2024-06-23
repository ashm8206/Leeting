class Solution:
    def minSwaps(self, s: str) -> int:
        left, right = 0, 0

        for _s in s:
            if _s=='[':
                right+=1
            elif  _s==']' and right > 0:
                right-=1
            else:
                left+=1
        #print(left)
        #return (left +1)//2
        return ceil(left/2)
