class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dict_set = set(dictionary)
        @lru_cache()
        def helper(start):

            if start >= n:
                return 0
            
            ans = 1 + helper(start+1) # Skip

            for end in range(start+1, n+1):
                curr_word = s[start:end]
                if curr_word in dict_set:
                    # Skip and not Skipped
                    ans = min(ans, helper(end))
            return ans
            # for end in range(start, n):
            #     curr_word = s[start:end+1] be careful of end+1
            
        return helper(0)
                
