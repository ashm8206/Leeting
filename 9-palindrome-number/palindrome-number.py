class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        ls = []
        reversedNum = 0 
        original_num = x
        while x:
            x, r = divmod(x, 10)
            reversedNum = reversedNum * 10 + r
        
        return original_num == reversedNum
            
        
