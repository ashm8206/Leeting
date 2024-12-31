class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = abs(n) 

        ans = 1
        
        def helper(n) -> float:
            if n == 0:
                return 1

            half = helper(n//2)

            if n%2:
               return half * half * x
            else:
                return half * half

        return helper(n)



        # nn = n
        while nn:

            if nn%2:
                ans = ans * x
                nn -=1
            else:
                x = x * x
                nn = nn // 2
        return ans

        

      