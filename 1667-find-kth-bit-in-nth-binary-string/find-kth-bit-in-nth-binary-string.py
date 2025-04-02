class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def helper(n, k):
            if n==1:
                return "0"
            
            length = 2**n - 1
            half = length // 2 
            if k<=half:
                return helper(n-1,k)
            elif k > half + 1:
                res = helper(n-1, length -  (k-1) ) 
                # k is 1-index, but deduct 0 index

                # helper(n-1,val) # val has to be 1 indexed
                
                return "0" if res== "1" else  "1"
            else:
                return "1" # at half + 1, center

        return helper(n, k)

        # def revInv(bin_string):
        #     new_string = ""
        #     for bit in bin_string:
        #         if bit=="1":
        #             new_string += "0"
        #         else:
        #             new_string += "1"
        #     return new_string[::-1]
        
        # def helper(i, prev):

        #     if i==n:
        #         return prev[k-1]
        #     return helper(i+1, prev + "1" + revInv(prev))

        # return helper(1, "0")