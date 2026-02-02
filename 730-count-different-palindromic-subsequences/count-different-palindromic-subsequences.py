class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(left, right):
            if left >= right:
                return 0
            
            count = 0
            
            for ch in 'abcd':
                # Find first and last occurrence of ch in range [left, right)
                first = s.find(ch, left, right)
                last = s.rfind(ch, left, right)
                
                if first == -1:
                    # Character not found
                    continue
                elif first == last:
                    # Found exactly once: single char palindrome
                    count += 1
                else:
                    # Found multiple times: count inner + add "a" and "aa"
                    # a - Palindorm
                    #"aa" - 2nd palindrome
                    count += dp(first + 1, last) + 2
            
            return count % MOD
        
        return dp(0, len(s))