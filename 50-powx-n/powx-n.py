class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = abs(n) 
        
        # def helper(n) -> float:
        #     if n == 0:
        #         return 1

        #     half = helper(n//2)

        #     if n%2:
        #        return half * half * x
        #     else:
        #         return half * half

        # return helper(n)

        result = 1
        while n != 0:
            # If 'n' is odd we multiply result with 'x' and reduce 'n' by '1'.
            if n % 2 == 1:
                result *= x
                # n -= 1
            # We square 'x' and reduce 'n' by half, x^n => (x^2)^(n/2).
            x *= x
            n //= 2
        return result


        # ans = 1
        # nn = n
        # while nn:

        #     if nn%2:
        #         ans = ans * x
        #         nn -=1
        #     else:
        #         x = x * x
        #         nn = nn // 2
        # return ans

        

      