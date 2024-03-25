from collections import deque
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # if len(num2) > len(num1):
        #     num1, num2 = num2, num1
        
        # res = []
        # carry = 0
        # num1 = num1[::-1]
        # num2 = num2[::-1]
        # for i, digit2 in enumerate(num2):
        #     # inter = deque()
        #     inter = ""
        #     for digit1 in num1:

        #         if carry: 
        #             val = int(digit1)*int(digit2) + carry 
        #         else:
        #             val = int(digit1)*int(digit2) 
                
        #         carry, mul = divmod(val,10)
        #         # print(digit1,digit2)
        #         inter = str(mul) + inter
                
        #     # print(inter)
        #     res.append((inter + "0"*i)) # find a fix for this step

        # print(res)
        # # input : ['738', '6150', '49200']
        # #  M*M to sum these
        # # TC TIME :  O(M⋅(N+M))
        
        # return ""

        # SOLUTION:  TC TIME :  O(M⋅N)

         # Initialize answer as a string of zeros of length N.

        if num1 == "0" or num2 =="0":
            return "0"

        N = len(num1) + len(num2)
        answer = [0] * N

        first_number = num1[::-1]
        second_number = num2[::-1]

        for place2, digit2 in enumerate(second_number):
            # For each digit in second_number multiply the digit by all digits in first_number.
            for place1, digit1 in enumerate(first_number):

                # The number of zeros from multiplying to digits depends on the place
                # of digit2 in second_number and the place of the digit1 in first_number.

                num_zeros = place1 + place2

                # The digit currently at position numZeros in the answer string
                # is carried over and summed with the current result.
                carry = answer[num_zeros]

                multiplication = int(digit1) * int(digit2) + carry

                # Set the ones place of the multiplication result.
                answer[num_zeros] = multiplication % 10
                
                # Carry the tens place of the multiplication result by 
                # adding it to the next position in the answer array.
                answer[num_zeros + 1] += multiplication // 10

        # Multiplication of 2 numbers of Len N and M
        #  Will have answer size [n+M-1, N+M] --> Not less than N+M - 1
        # unless any of the numbers is "Zero"

        # Therefore, just One fi statement to Pop zero is enough
        #  while is not required

        if answer[-1] == 0:
            answer.pop()

        return "".join(str(digit) for digit in answer[::-1])