class Solution:
    def reverseBits(self, n: int) -> int:
        ret,  power = 0, 31

        while n:
            ret += (n & 1) << power
            # (n & 1) << power only adds to ret when the current bit is 1
            n = n >> 1
            power-=1
        return ret