class Solution:
    def firstUniqChar(self, s: str) -> int:
        left = defaultdict(int)
        count = defaultdict(int)

        minIdx = len(s)

        for i, ch in enumerate(s):
            if ch in left:
                count[ch]+=1
            else:
                left[ch] = i
                count[ch] = 1
        
        for ch in s:
            if count[ch]==1:
                return left[ch]
        return -1
    










        # count = {}
        # left = {}

        # for i, ch in enumerate(s):
        #     if ch not in left:
        #         left[ch]=i
        #     count[ch]= count.get(ch,0) + 1

        
        # for ch in s:
        #     if count[ch]==1:
        #         return left[ch]
        # return -1

