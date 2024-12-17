class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        maxheap = [(-ord(c), cnt) for c, cnt in Counter(s).items()]
        heapify(maxheap)
        result = []

        while maxheap:
            charOrd, count = heappop(maxheap)
            char = chr(-charOrd)
            use = min(count, repeatLimit)
            result.append(char*use)

            if count > use and maxheap:
                charOrdNext, countNext = heappop(maxheap)
                charNext = chr(-charOrdNext)
                result.append(charNext)
            
                if countNext - 1 > 0:
                    heappush(maxheap, (charOrdNext, countNext - 1))
                # count-use will always be > 0
                # count - use > use - use
                # i.e count > 0
                heappush(maxheap, (charOrd, count-use))

        return "".join(result)
