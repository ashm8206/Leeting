class Solution:
    def countGoodNumbers(self, n: int) -> int:
        

    
        

    
        #. =  # Een positions for ODD and EVEN lens = (N+1)//2
        # 0, 2, 4, 6, 8
        # 2, 3, 5, 7
        
        MOD = 10 ** 9 + 7
        def fastPower(x, n):
            ans = 1
            while n:
                if n%2 == 1:
                    ans = (ans * x)%MOD
                x = (x * x ) % MOD
                n //= 2
            return ans 

            # ret = 1
            # mul = x
            # while n:
            #     if n%2==1:
            #         ret = ret * mul % MOD
            #     mul = mul * mul % MOD
            #     n = n // 2
            # return ret
        



        return fastPower(5, (n + 1) // 2) * fastPower(4, n // 2) % MOD



        # x = 4*5
        # def fastPower(x, n):
        #     sums = 1
        #     while n:
        #         if n%2:
        #             sums = (x * sums) % MOD 
        #             # for even it will come to 1 and 1*Doublled stuff
        #             n -=1
        #         else:
        #             x = (x * x) % MOD
        #             n //= 2
        #     return sums % MOD

        # oddLen = 0 if n % 2 == 0  else 1

        # if oddLen:
            
        #     return (fastPower(x, n//2) * 5) % MOD # Multiple by 5 as its odd len
        # else:
        #     return fastPower(x, n//2)


    
            

       
        # https://leetcode.com/problems/count-good-numbers/solutions/1314363/java-python-3-iterative-o-logn-code-similar-to-lc50-pow-x-n-w-brief-explanation-and-analysis/


        # Time 0(N)
        # Space = O(1)


