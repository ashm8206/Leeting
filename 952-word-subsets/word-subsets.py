class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans
        
        bmax = [0] * 26
        for b in words2:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        result = []

        
        for word in words1:
            if all(cnt1 >= cnt2 for cnt1, cnt2 in zip(count(word),bmax)):
                result.append(word)
        return result
