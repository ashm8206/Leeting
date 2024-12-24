class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        lineSweep = SortedDict({0: 0})
        for start, end in flowers:
            lineSweep[start] = lineSweep.get(start, 0) + 1
            lineSweep[end + 1] = lineSweep.get(end + 1, 0) - 1
        
        positions = []
        prefix = []
        curr = 0
        for key, val in lineSweep.items():
            positions.append(key)
            curr += val
            prefix.append(curr)

        ans = []
        for person in people:
            i = bisect_right(positions, person) - 1
            ans.append(prefix[i])
        
        return ans