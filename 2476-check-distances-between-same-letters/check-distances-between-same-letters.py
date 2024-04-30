class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        
        # idx in Hmap check distance[i] == end-start-1
        # Hmap --> add s[i] idx to map [start,end]
        
        hmap = {}
        for i, char in enumerate(s):
            idx = ord(char)-ord('a')
            if idx not in hmap:
                hmap[idx] = [i,0] #[Start,end]
            else:
                hmap[idx][1] = i # set end

        for key, val  in hmap.items():
            start, end = val
            if distance[key]!=  end-start-1:
                return False
        return True