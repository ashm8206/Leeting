from collections import defaultdict
class Solution:
    def nextGreaterElement(self, n: int) -> int:

        digits = list(str(n))
        n = len(digits)

        i = j = n-1

        while i > 0 and digits[i-1] >= digits[i]:
            i -= 1

        if i == 0:   # nums are in descending order
            return -1
        
        k = i - 1    # find the last "ascending" position
        while digits[j] <= digits[k]:
            j -= 1

        digits[k], digits[j] = digits[j], digits[k] 

        # i = n - 1
        # while i-1>= 0 and digits[i-1]>=digits[i]:
        #     i-=1

        # if i == 0:
        #     return -1
        
        # j = i
        # # i....n
        # # last digit > digits[i-1]
        # # last digit > 5

        # while j+1 < n and digits[j+1] > digits[i-1]:
        #     j+=1
        # digits[i-1], digits[j] =   digits[j], digits[i-1]
        digits[i:] = digits[i:][::-1]
        ret = int(''.join(digits))

        return ret if ret < 1<<31 else -1

        # s = str(n)
        # lenS = len(s)

        # res = []
        # countMap = Counter(s)
        # def helper(slate):
        #     if len(slate) == lenS:
        #         res.append(int("".join(slate[:])))
        #         return
            
        #     for val in countMap.keys():
        #         if countMap[val] <= 0 :
        #             continue
        #         slate.append(val)
        #         countMap[val]-=1
        #         helper(slate)
        #         slate.pop()
        #         countMap[val]+=1
        
        # helper([])
        # res.sort()
        # idx = res.index(n) + 1
        
        # return  -1  if idx >= len(res) or res[idx] >= 2**31 else res[idx]