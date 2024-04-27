class LargerNumber(str):
        def __lt__(x,y):
            # x < y ? 
            # 2,10 #  take 2 first, in the generator
            # x+ y > y + x -->  True
            # Return 
            return x+y > y+x
            # https://www.youtube.com/watch?v=WDx6Y4i4xJ8
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        # Its a Bit Mathy
        #  10 < 2 ? -->  10 > 2
        # 102 > 210

        # 9 5,3,30 34 
        # If AB > BA and BC > CB, then we have AC > CA.
        #  95 > 59
        #  53 > 35
        # hence 93 > 39

        # print(sorted([ '9','5','34','3','30'], reverse = True))
        largest_num = ''
        largest_num = ''.join(sorted(map(str,nums),key=LargerNumber))
        return '0' if largest_num[0]=='0' else largest_num