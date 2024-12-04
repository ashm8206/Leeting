class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        arr = list(bin(n))[2:]
        if len(arr) < 32:
            arr= ['0']*(32-len(arr)) + arr
        
        for i in range(16):
            arr[i], arr[31-i] = arr[31-i], arr[i]
        # print(arr)
        return int("".join(arr),2)
     
        