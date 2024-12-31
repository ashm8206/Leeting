class Solution:
    def numberToWords(self, num: int) -> str:
        array_below_10 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        array_below_20 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        array_below_100 = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


        def helper(num):

            if num < 10:
                return array_below_10[num]
            if num < 20:
                return array_below_20[num%10]
            if num < 100:
                return array_below_100[num//10] + (" " + helper(num%10) if num%10!=0 else "")
            if num < 1000:
                return helper(num//100) + " Hundred" + (" " + helper(num%100) if num%100!=0 else "")
            if num < 1000000:
                return  helper(num//1000) + " Thousand" +  (" " + helper(num%1000) if num%1000 > 0 else "") 
            if num < 1000000000:
                return helper(num//1000000) + " Million" +  (" " + helper(num%1000000) if num%1000000 !=0 else "") 

            return helper(num//1000000000) + " Billion" +  (" " + helper(num%1000000000) if num%1000000000!=0 else "") 
        
        if num == 0:
            return "Zero"
        return helper(num)