class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        # Method I

        # arr = list(bin(n))[2:]
        # if len(arr) < 32:
        #     arr= ['0']*(32-len(arr)) + arr
        
        # for i in range(16):
        #     arr[i], arr[31-i] = arr[31-i], arr[i]
        # # print(arr)
        # return int("".join(arr),2)

        # Method II
        ret, power = 0, 31
        while n:

            # isolate the LSB
            ret += (n & 1) << power
            power -=1
            n >>= 1
        return ret

     
        