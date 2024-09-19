class LargerNumber(str):
        def __lt__(x,y):
            # x < y ? 
            #  2 < 10 ?


            # https://blog.cambridgespark.com/magic-methods-a8d93dc55012
            # 210 < 102 ?  no, so 2 is not less 10
            return x+y < y+x
            # https://www.youtube.com/watch?v=WDx6Y4i4xJ8
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:


        # 9 5,3,30 34 
        # If AB > BA and BC > CB, then we have AC > CA.
        #  95 > 59
        #  53 > 35
        # hence 93 > 39

        # print(sorted([ '9','5','34','3','30'], reverse = True))
        largest_num = ''
        largest_num = ''.join(sorted(map(str,nums),key=LargerNumber, reverse = True))
        return '0' if largest_num[0]=='0' else largest_num

        # https://leetcode.com/problems/largest-number/solutions/213599/thinking-process-in-python/

        # return "".join(sorted(map(str, nums), cmp=lambda n1, n2: -1 if n1+n2 > n2+n1 else (1 if n1+n2<n2+n1 else 0))) -> reverse is mising

