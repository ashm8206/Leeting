class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        result = []

        def helper(slate, l, r):
            if l > r:
                result.append("".join(slate[:]))
                return
            
            if l == r:
                slate[l]="0"
                result.append("".join(slate[:]))
                slate[l]="1"
                result.append("".join(slate[:]))
                slate[l]="8"
                result.append("".join(slate[:]))
                return 
            
            if l!=0:
                slate[l] = '0'
                slate[r] = '0'
                helper(slate, l + 1, r - 1)

            slate[l] = '1'
            slate[r] = '1'
            helper(slate, l + 1, r - 1)

            slate[l] = '8'
            slate[r] = '8'
            helper(slate, l + 1, r - 1)

            slate[l] = '6'
            slate[r] = '9'
            helper(slate, l + 1, r - 1)

            slate[l] = '9'
            slate[r] = '6'
            helper(slate, l + 1, r - 1)
                
        
        helper([""]*n, 0, n-1)
        return result