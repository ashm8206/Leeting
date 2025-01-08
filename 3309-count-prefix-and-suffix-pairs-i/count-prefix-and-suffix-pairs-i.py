class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(str1, str2):
            
            return str2.startswith(str1) and str2[-len(str1):].startswith(str1)
        
        count = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1,n):
                count+=isPrefixAndSuffix(words[i], words[j])
                # print(words[i], words[j], isPrefixAndSuffix(words[i], words[j]))
        return count
