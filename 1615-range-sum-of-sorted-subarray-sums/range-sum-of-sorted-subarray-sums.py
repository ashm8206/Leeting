class Solution:

    import heapq

    def rangeSum(self, nums, n, left, right):
        pq = []
        for i in range(n):
            heapq.heappush(pq, (nums[i], i))

        ans = 0
        mod = 1e9 + 7
        for i in range(1, right + 1):
            currSum, index = heapq.heappop(pq)
            # If the current index is greater than or equal to left, add the
            # value to the answer.
            if i >= left:
                ans = (ans + currSum) % mod
            # If index is less than the last index, increment it and add its
            # value to the first pair value.
            if index < n - 1:
                p = (currSum + nums[index + 1], index + 1)
                heapq.heappush(pq, p)
        return int(ans)

    # Brute
    # def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
    #     n = len(nums)

    #     def get_prefix_sum(arr) -> List[int]:
    #         n = len(arr)
    #         prefix_sum = [0] * n
    #         prefix_sum[0] = arr[0]

    #         for i in range(1,n):
    #             prefix_sum[i] = prefix_sum[i-1] + arr[i]

    #         return prefix_sum
        
    #     prefix = get_prefix_sum(nums)
    #     total_sums = []
    #     for i in range(n):
    #       for j in range(i, n):
    #         if i > 0:
    #             total_sums.append(prefix[j]-prefix[i-1])
    #         else:
    #             total_sums.append(prefix[j])

    #     total_sums.sort()
    #     prefix_total = get_prefix_sum(total_sums)


    #     left = left - 1
    #     right = right - 1

    #     return  (prefix_total[right] - prefix_total[left-1] if left > 0 else prefix_total[right]) % (10**9 + 7)
