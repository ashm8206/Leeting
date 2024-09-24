class Solution:
    def countAndSay(self, n: int) -> str:

        # Iterative
        def getRunLen(rle_str):

            #  Method I
            # rle_str = deque(list(rle_str))
            # # rle_str = list(rle_str)
            # stack = []
            
            # while rle_str:
            #     var = rle_str.popleft()
            #     # var = rle_str.pop(0)
            #     if stack and stack[-1][0] == var:
            #         stack[-1][1]+=1
            #     else:
            #         stack.append([var, 1])
            # RLE = "".join( str(y) + x  for x, y in stack)

            stack = []
            n = len(rle_str)
            cnt = 1
            for i in range(0, n):
                if i < n-1 and rle_str[i]==rle_str[i+1]:
                    cnt+=1
                else:
                    stack.append(str(cnt))
                    stack.append(rle_str[i])
                    cnt = 1
            
            return "".join(stack)

        RLE = '1'
        while n > 1:
            RLE = getRunLen(RLE)
            n-=1 
        return RLE

        # Recursive
        # def rle(s):
        #     count = 1
        #     ret = []
        #     n = len(s)-1
        #     for i in range(0,n+1):
        #         if i<n and s[i] == s[i+1]:
        #             count += 1
        #         else:
        #             ret.append(str(count))
        #             ret.append(s[i])
        #             count = 1
        #     return "".join(ret) 
        
        # if n == 1:
        #     return "1"
        # return rle(self.countAndSay(n-1))