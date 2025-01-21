class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
     
        row_sum = map(sum, grid)
        col_sum = map(sum, zip(*grid)) 
        # syntax sugar learned from stefan :-)

        def minTotalDistance1D(vec):
            i, j = -1, len(vec)
            d = left = right = 0
            while i != j:
                if left < right:
                    d += left
                    i += 1
                    left += vec[i]
                else:
                    d += right
                    j -= 1
                    right += vec[j]
            return d

        return minTotalDistance1D(list(row_sum)) + minTotalDistance1D(list(col_sum))


# 57 / 57 test cases passed.
# Status: Accepted
# Runtime: 40 ms