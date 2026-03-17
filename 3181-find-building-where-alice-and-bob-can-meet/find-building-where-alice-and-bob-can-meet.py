import bisect
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # [6,4,8,5,2,7]
        # 1. Queries, sorted on x[0]
        # 1a. if x == y ans is y
        # 2. if heights[x] < heights[y] 
        # 3. else: t > y such that height[t] next greater for [y...N]

        mono_stack = []
        n = len(queries)
        result = [-1 for _ in range(n)]
        new_queries = [[] for _ in range(len(heights))]

        for i in range(n):
            a = queries[i][0]
            b = queries[i][1]
            if a > b:
                a, b = b, a
            if heights[a] < heights[b] or a == b:
                result[i] = b
            else:
                # heights[a] >= heights[b] 
                # both alice and bob have to travel left
                new_queries[b].append((heights[a], i))

        # store the queries
        # find next greater
        for i in range(len(heights) - 1, -1, -1):
            mono_stack_size = len(mono_stack)
            for a, b in new_queries[i]:
                position = self.search(a, mono_stack)

                if position < mono_stack_size and position >= 0:
                    result[b] = mono_stack[position][1] # This [1] is the [(7, 5)] position 7 is at
            # for t right of this y index,
            #.  for height[x], y index in new_queries[i]
            #.     find height[t] >  height[x] with bineary search

            # print(heights[i], new_queries[i], mono_stack)
            while mono_stack and mono_stack[-1][0] <= heights[i]:
                mono_stack.pop()
            mono_stack.append((heights[i], i))
        return result

    def search(self, height, mono_stack):
        left = 0
        right = len(mono_stack) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mono_stack[mid][0] > height:
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans