class Solution:
    def countAndSay(self, n: int) -> str:

        def getRunLen(rle_str):
            rle_str = deque(list(rle_str))
            stack = []
            
            while rle_str:
                var = rle_str.popleft()
                if stack and stack[-1][0] == var:
                    stack[-1][1]+=1
                else:
                    stack.append([var, 1])
            RLE = "".join( str(y) + x  for x, y in stack)
            
            return RLE

        RLE = '1'
        while n > 1:
            RLE = getRunLen(RLE)
            n-=1 
        return RLE