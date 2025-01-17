class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        # remove_dict = {r : i for i, r in enumerate(removable)}
        # def check(last_removable):
        #     i,j = 0,0

        def check(m):
            i = j = 0
            remove = set(removable[:m+1])
            while i < len(s) and j < len(p):
                # if i in remove_dict and remove_dict[i] <= last_removable:
                if i in remove:
                    i += 1
                    continue
                if s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(p):
                return True
            return False
        lo = 0
        hi = len(removable)
        while lo < hi:
            mi = (lo+hi) // 2
            if check(mi):
                lo = mi+1
            else:
                hi = mi
        return lo
                