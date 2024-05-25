class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        res = []
        n = len(str(low))
        m = len(str(high))

        ls = '123456789'


        for step in range(n,m+1):
            for i in range(len(ls)-step+1):
                candidate = int(ls[i:i+step])

                # print(candidate)

                if candidate < low:
                    continue
                elif candidate > high:
                    break
                else:
                    res.append(candidate)
        return res

                

