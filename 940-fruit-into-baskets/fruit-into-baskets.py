class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        hmap = defaultdict(int)
        n = len(fruits)
        l = 0
        maxNum = 0
        numBasket = 2

        for r in range(n):
            hmap[fruits[r]] = hmap[fruits[r]] + 1

            while len(hmap) > numBasket:
                hmap[fruits[l]]-=1
                if hmap[fruits[l]] == 0:
                    del hmap[fruits[l]]
                l+=1
            maxNum = max(maxNum, r-l+1)
        return maxNum