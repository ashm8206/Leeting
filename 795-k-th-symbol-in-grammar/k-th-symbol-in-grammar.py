class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

    # 0 : 2^0
    # 01 : 2^1
    # 0110 :2^2
    # 0110 1001: 2^3

    # 1,2,3,4
    # 5,6,7,8
    # half + delta = k
    # # k - half

        def helper(n, k):
            if n==1:
                return 0
            
            length = 2**(n-1)
            half = length //2

            if k <= half:
                return helper(n-1, k)
            else:
                res = helper(n-1, k-half)
                return 0 if res==1 else 1
        return helper(n,k)
        


        
       