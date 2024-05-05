class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # b: 1
        # a: 1
        # l: N//2 Min
        # o: N//2
        # n: 1

        hmap = {}
        for char in text:
            if char in 'balon':
                hmap[char] = hmap.get(char,0)+1
        
        if len(hmap)!=5:
            return 0
        minCount = 10**4
        for k, v in hmap.items():
            if k in ('l','o'):
                v = v//2
            minCount = min(v,minCount)
            # print(minCount)
        return minCount if minCount!=10**4 else 0
