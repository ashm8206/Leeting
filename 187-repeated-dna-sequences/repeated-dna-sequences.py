class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        n = len(s)

        res = set()

        maps = set()
        for start in range(n-L+1):
            cand_str = s[start:start+L]
            # print(cand_str)

            if cand_str in maps and cand_str not in res:
                res.add(cand_str)

            maps.add(cand_str)
        return res
