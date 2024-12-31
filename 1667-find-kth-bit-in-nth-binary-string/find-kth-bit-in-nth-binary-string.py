class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def revInv(bin_string):
            new_string = ""
            for bit in bin_string:
                if bit=="1":
                    new_string += "0"
                else:
                    new_string += "1"
            return new_string[::-1]
        
        def helper(i, prev):

            if i==n:
                return prev[k-1]
            return helper(i+1, prev + "1" + revInv(prev))

        return helper(1, "0")