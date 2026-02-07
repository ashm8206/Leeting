class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        

        
        

        min_y = float("inf")
        max_y, total_area = 0, 0
        for x, y, l in squares:
            total_area += l**2
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)

        def feasible(mid):
            area = 0
            for x, y, l in squares:
                if y < mid:
                    area += l * min(mid - y, l)
            return area >= total_area / 2

        l = min_y
        r = max_y
        eps = 10**-5
        while abs(r - l) > eps:
            mid = (l+r)/2
            if feasible(mid):
                r = mid
            else:
                l = mid
        return l