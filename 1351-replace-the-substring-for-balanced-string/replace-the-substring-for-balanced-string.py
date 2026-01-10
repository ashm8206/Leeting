from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        k = n/4
        hmap = Counter(s)

        alreadyBalanced = all(val==k for key, val in hmap.items())
        if alreadyBalanced: 
            return 0
        

        l = 0
        extra = defaultdict(int)
        min_len = float("inf")


        for r in range(n):
            extra[s[r]] +=1

            # hmap['Q'] - extra['Q'] > k  # that means you have more than K chars
            # outside the extra substring
            
            # Outside Must be:
            # outside == k 
            # outside  < k : which extra chars can provide
            
            while  l <= r and (
                hmap['Q'] - extra['Q'] <= k 
                and hmap['R'] - extra['R'] <= k
                and hmap['E'] - extra['E'] <= k
                and hmap['W'] - extra['W'] <= k

            ):
                
                min_len = min(min_len, r-l+1)
                extra[s[l]]-=1
                l+=1
        return min_len
                

       
        
