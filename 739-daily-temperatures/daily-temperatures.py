class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        res = [0] * n   
        stack = []

        for i in range(n):
            # next Greater element 
            # Strictly Greater
            # decreasing array
            while stack and temperatures[stack[-1]] < temperatures[i]:
                stackTopIdx = stack.pop()
                # number of days in the ans
                res[stackTopIdx] = i - stackTopIdx
            
            stack.append(i)
        return res

        # for i in range(n):
        #     while stack and temperatures[stack[-1]] < temperatures[i]:
        #         day = stack.pop()
        #         res[day] = i-day
        #     stack.append(i)
        # return res 
      