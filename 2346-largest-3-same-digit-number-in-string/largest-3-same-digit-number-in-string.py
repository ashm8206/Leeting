class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        c = ''
        maxNum = -1
        for i in range(len(num)):
            if i and num[i-1]!=num[i]:
                if len(c) >= 3:
                    candidate = ord(c[0]) - ord('0')
                    maxNum = max(maxNum, candidate)
                c = num[i]
            else:
                c+=num[i]

        # print(c,maxNum)

        if len(c) >= 3:
            candidate = ord(c[0]) - ord('0')
            maxNum = max(maxNum, candidate)
        
        if maxNum!=-1:
            return str(maxNum)*3
        else:
            return ""

        