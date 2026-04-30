class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        # cost = 0
        # n = len(arr)
        # if arr == brr:
        #     return cost 
    
        
        # # 1. Find the order of indices that would sort brr descending
        # # This tells us: "The largest value is at index 0, the next at index 2, etc
        # order = sorted(range(len(brr)), key=lambda i: brr[i], reverse=True)

        # # 2. Sort arr descending
        # arr_sorted = sorted(arr, reverse=True)

        

        # # 3. Place the sorted values of arr into the result based on brr's order
        # shuffled = [0] * len(arr)
        # for rank, original_index in enumerate(order):
        #     shuffled[original_index] = arr_sorted[rank]

        # cost1 = k + sum(abs(shuffled[i]- brr[i]) for i in range(n))
        # cost2 = sum(abs(arr[i]- brr[i]) for i in range(n))
        # return min(cost1, cost2)

        res1 = sum(abs(a - b) for a, b in zip(arr, brr))
        res2 = sum(abs(a - b) for a, b in zip(sorted(arr), sorted(brr)))
        return min(res1, res2 + k)