from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:

        rightCount = Counter(s)
        leftCount = defaultdict(int)
        n = len(s)
        count = 0
        for i in range(n):
            leftCount[s[i]]+= 1
            rightCount[s[i]] -=1
            if rightCount[s[i]] == 0:
                del rightCount[s[i]]
            
            count += 1 if len(leftCount.keys())== len(rightCount.keys()) else 0
        return count



        # n = len(s)
        # count = 0
        # for i in range(1, n):
        #     set1 = set(s[:i])
        #     set2 = set(s[i:])
        #     if len(set1) == len(set2):
        #         count+=1
        # return count

    