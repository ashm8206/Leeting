class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n==0:
            return 1

        mask = 1
        num = n

        while num:
            num >>=1
            mask <<=1
        # print(mask-1, n)
        # print(0^0)
        # xor Same = 0
        # diff: 1
        return n ^ (mask-1)