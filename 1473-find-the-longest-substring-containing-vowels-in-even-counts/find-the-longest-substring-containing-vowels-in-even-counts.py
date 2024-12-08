class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        # Method I
        maxStrLen = 0
        n = len(s)
        # for st in range(n):
        #     for e in range(st, n):
        #         mask = {"a":0,"e":0,"i":0,"o":0,"u":0}
        #         for k in range(st, e+1):
        #             if s[k] in mask.keys():
        #                 mask[s[k]]^=1
                
        #         if e-st+1 > maxStrLen :
        #             if sum(mask.values())==0:
        #                 maxStrLen = max(maxStrLen, e-st+1)
        # return maxStrLen

        charMap = [0]*26
        charMap[ord("a")-ord("a")] = 16
        charMap[ord("e")-ord("a")] = 8
        charMap[ord("i")-ord("a")] = 4
        charMap[ord("o")-ord("a")] = 2
        charMap[ord("u")-ord("a")] = 1

        longestSubString = 0
        prefixXor = 0
        prefixXorMap = {0:-1}
        for i in range(n):
            prefixXor ^= charMap[ord(s[i])-ord("a")]

            if prefixXor== 0 or prefixXor in prefixXorMap:
                longestSubString = max(longestSubString, i-prefixXorMap[prefixXor]) 
                # okay, its between them indexes of Same Prefx, this has taken place
            else:
                # seeing first time, only then cache
                prefixXorMap[prefixXor] = i
        return longestSubString

