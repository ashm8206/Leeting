class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        res = set()
        for str1 in words:
            for str2 in words:
                if str1 in str2 and str1!=str2:
                    res.add(str1)
        return list(res)