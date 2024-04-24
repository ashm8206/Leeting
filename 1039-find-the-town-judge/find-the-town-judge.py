class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg = defaultdict(list)
        trusting = set()

        for u, v in trust:
            indeg[v].append(u)
            trusting.add(u)

        for i in range(1,n+1):
            length = len(indeg.get(i,[]))
            if length==n-1 and i not in trusting:
                return i
        return -1

        