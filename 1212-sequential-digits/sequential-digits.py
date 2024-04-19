class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        res = []
        n = len(str(low))
        m = len(str(high))

        ls = '123456789'

        # print(len(ls),m)

        for step in range(n,m+1):
            for i in range(len(ls)-step+1):
                candidate = int(ls[i:i+step])

                print(candidate)

                if candidate < low:
                    continue
                elif candidate > high:
                    break
                else:
                    res.append(candidate)
        return res

                


        # len(10, 1000)
        # for step in range len(2, 4)
        # for i in range(9-step) ls = 123456789
        #    candidate = ls[i:i+step]
        #    if int(candidate) < low:
        #       continue
            # elif int(candidate) > high:
            # break
            # else: append
        #   234
        #    345