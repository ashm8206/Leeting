class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        # Method I - Brute force N^3

        # n = len(s)
        # l = 0
        # # hmap = defaultdict(int)
        # maxLen = 0
        # for l in range(n):
        #     hmap = defaultdict(int)
        #     for r in range(l, n):
        #         hmap[s[r]]+=1

        #         if r-l+1 >= k*len(hmap):
        #             # check freq of each candidate
        #             all_greater = all([ val >= k for key, val in hmap.items()])
        #             if all_greater:
        #                 maxLen = max(maxLen, r-l+1)
        # return maxLen

    #  Method II - Divide and conquer

        # if len(s) < k:
        #     return 0

        # counter = defaultdict(int)

        # for char in s:
        #     counter[char]+=1
        
        # for i, char in enumerate(s):
        #     if counter[char] < k:
        #         left = self.longestSubstring(s[:i], k)
        #         right = self.longestSubstring(s[i+1:], k)
        #         return max(left, right)

        # return len(s)

        # Method III  - Another helper

        def helper(st, e, k):
            if e - st < k:
                return 0
            counter = defaultdict(int)

            for i in range(st, e):
                counter[s[i]] +=1

            for mid in range(st, e):
                # [st..mid)  and [midNext+1..e) --> e in len(s)
                if counter[s[mid]] < k:
                    midNext = mid+1
                
                    while midNext < e and counter[s[midNext]] < k:
                        midNext+=1
                        # Keep skiping all invalid char, they are of no use to us
                    return max(helper(st,mid, k), helper(midNext, e, k))
            return e - st # no need to add +1 as end  is already +1 due to len      
        return helper(0, len(s), k)
