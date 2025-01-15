class Solution:
    def intToRoman(self, num: int) -> str:

        # Problem of ambiguity
        #  140 : L L X  (50 + 50 + 10)
        #  140 : CXL  (100+ 40)
        # 140 : CXXX  (100+ 10+10+10)

        digits = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        res = []

        for val, symb in digits:
            count, num = divmod(num, val)
            # print(count, num, val)
            res.append(count * symb)
        
        return "".join(res)


        # roman_digits = []
        # # Loop through each symbol.
        # for value, symbol in digits:
        #     # We don't want to continue looping if we're done.
        #     if num == 0:
        #         break
        #     # Q, Remainder = divmod(num, value)
        #     count, num = divmod(num, value)
        #     # Append "count" copies of "symbol" to roman_digits.
        #     roman_digits.append(symbol * count)
        # return "".join(roman_digits)