class Solution:
    def divide(self, dividend: int, divisor: int) -> int:


        # TLE
        # exactly 1 -ve add Negative sign  add -ve at end
        # negative = 0
    
        # if dividend < 0:
        #     negative+=1

        # if divisor < 0:
        #     negative+=1
        
        # quotient = 0

        # while dividend - divisor >=0:
        #     dividend -= divisor 
        #     quotient+=1

        # if negative%2:
        #     return quotient * -1
        # else:
        #     return quotient

        # method II 
        # Special case when dividend is equal to divisor
        if dividend == divisor:
            return 1

        # Determine if the result will be positive or negative
        is_positive = (dividend < 0) == (divisor < 0)  # True if same sign

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0 
        while dividend >= divisor:
            power_of_two = 1
            value = divisor

            # Double the value while it is still smaller than the dividend
            while value + value <= dividend:
                value += value
                power_of_two += power_of_two

            # Add the power of two multiples of divisor to the quotient
            quotient += power_of_two

            # Subtract the value so far from the dividend
            dividend -= value


        # # If the result overflows, return INT_MAX (edge case)
        if quotient == (1 << 31):
            if is_positive:
                return (1 << 31) - 1  # Return INT_MAX
            else:
                return -(1 << 31) 
        # MAX_INT = 2147483647  # 2**31 - 1
        # MIN_INT = -2147483648  # -2**31

        # Return the result, considering the sign
        return quotient if is_positive else -quotient



        
        