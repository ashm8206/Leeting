class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        counter = [0]*3

        for c in s:
            counter[ord(c) - ord("a")] += 1

        for i in range(3):
            if counter[i] < k:
                return -1
        

        hmap = defaultdict(int)

        maxWindow = 0
        n = len(s)
        l = 0

        for r in range(n):
            hmap[s[r]] +=1

            while (l <= r and (
                counter[0] - hmap['a'] < k
                or counter[1] - hmap['b'] < k
                or counter[2] - hmap['c'] < k
            )):
                hmap[s[l]]-=1
                l+=1

            maxWindow = max(maxWindow, r-l+1)

        return n - maxWindow

