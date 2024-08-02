class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        
        hmap_cand_substr = defaultdict(set)
        hmap_str_cand = defaultdict(set) 
        

        for idx, cand in enumerate(arr):
            hmap_cand_substr[cand].add("")
            hmap_str_cand[""].add((cand, idx))
            for i in range(len(cand)):
                for j in range(i,len(cand)):
                    hmap_cand_substr[cand].add(cand[i:j+1])
                    hmap_str_cand[cand[i:j+1]].add((cand, idx))
        
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