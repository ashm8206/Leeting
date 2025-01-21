import heapq
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        heap = []
        output = 0
        for i in range(n):
            heap.append((reward2[i] - reward1[i], i))
        
        heapq.heapify(heap)
        visited = set()
        while k:
            k -= 1
            _, idx = heapq.heappop(heap)
            visited.add(idx)
            output += reward1[idx]
        
        for idx, val in enumerate(reward2):
            if idx in visited:
                continue
            output += val
        
        return output