class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}
        def helper(ind, m, n):
            if ind == len(strs):
                return 0
            if (ind, m, n) in cache:
                return cache[ind, m, n]
           
            count_0 = strs[ind].count("0")
            count_1 = len(strs[ind]) - count_0

            res = helper(ind + 1, m, n)

            if m >= count_0 and n >= count_1:
                res = max(res, 1 + helper(ind + 1, m - count_0, n - count_1))
            
            cache[ind, m, n] = res
            return cache[ind, m, n]
            
        return helper(0, m, n)