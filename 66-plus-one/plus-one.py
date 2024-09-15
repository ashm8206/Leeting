class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)
        
        last_digit = digits[-1] + 1

        carry , next_num = divmod(last_digit, 10)

        if n == 1:
            if carry:
                return [carry, next_num]
            else:
                return [last_digit]

        res = [next_num]

        for i in range(n-2, -1, -1):
            if carry:
                next_num = digits[i] + carry
            else:
                next_num = digits[i]
            carry, next_num = divmod(next_num, 10)
            res.append(next_num)
        
        return [carry] + res[::-1] if carry else res[::-1]

        # [9,9,9]


        

