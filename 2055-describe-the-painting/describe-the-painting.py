class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        mapping = defaultdict(int)
        # maxNum = -1
        # minNum = 10**6
        for s, e, c in segments:
            mapping[s] += c
            mapping[e] -= c
            # maxNum = max([maxNum, s, e])
            # minNum = min([minNum, s, e])
        
        res = []
        prev, color = None, 0

        for now, _ in sorted(mapping.items(), key = lambda x: x[0]):
        # for now in range(minNum, maxNum+1):
            # if now in mapping.keys():
            if color:
                res.append([prev, now, color])

            color += mapping[now]
            prev = now 
        return res 

        
        
