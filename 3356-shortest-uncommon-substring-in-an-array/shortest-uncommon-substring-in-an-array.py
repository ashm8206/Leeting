# My answer

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        
        hmap_cand_substr = defaultdict(set)
        hmap_str_cand = defaultdict(set) 
        

        for idx, cand in enumerate(arr):
            hmap_cand_substr[cand].add("")
            hmap_str_cand[""].add(idx)
            for i in range(len(cand)):
                for j in range(i,len(cand)):
                    hmap_cand_substr[cand].add(cand[i:j+1])
                    hmap_str_cand[cand[i:j+1]].add(idx)
        
        result  = []
        
        for cand in arr:
            found = False
            for value in sorted(hmap_cand_substr[cand], key= lambda x : (len(x), x)):
                if len(hmap_str_cand[value]) == 1:
                    result.append(value)
                    found = True
                    break
            if not found:
                result.append("")

        return result

        # Time: N* N**2LogN**2
        # Space : O(N*N): all substrings



# UpVoted answer Time Complexity ?

# class Solution:
#     def shortestSubstrings(self, arr: List[str]) -> List[str]:
#         def helper(s):
#             substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
#             return sorted(substrings, key=lambda x:(len(x), x))
        
        
        
#         n = len(arr)
#         ans = ["" for _ in range(n)]
        
#         for i in range(n):
#             all_str = helper(arr[i]);
#             for str1 in all_str:
#                 unique = True
#                 for j in range(n):
#                     if i != j and str1 in arr[j]:
#                         unique = False
#                         break
#                 if unique:
#                     ans[i] = str1
#                     break
                    
                    
#         return ans
    