class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        counter = Counter(s)

        for key, count in counter.items():
            if count < k:
                return -1

        if len(counter) < 3 and k!=0:
            return -1
        

        hmap = defaultdict(int)

        maxWindow = 0
        n = len(s)
        l = 0

        for r in range(n):
            hmap[s[r]] +=1

            while (l <= r and (
                counter['a'] - hmap['a'] < k
                or counter['b'] - hmap['b'] < k
                or counter['c'] - hmap['c'] < k
            )):
                hmap[s[l]]-=1
                l+=1

            maxWindow = max(maxWindow, r-l+1)

        return n - maxWindow

