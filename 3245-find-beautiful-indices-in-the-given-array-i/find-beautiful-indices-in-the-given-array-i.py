class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # [i...i+a.len] == a, then i is a candidate
        # [j...j+b.len] == b, then j is b candidate

        n = len(s)
        na = len(a)
        nb = len(b)

        beautList = []
        aIndexList = []
        bIndexList = []

        for i in range(n-na+1):
            curr_a = s[i:i+na]
            if curr_a==a:
                aIndexList.append(i)
        
        for j in range(n-nb+1):
            curr_b = s[j:j+nb]
            if curr_b==b:
                bIndexList.append(j)

        # print(aIndexList, bIndexList)
        for i in aIndexList:
            for j in bIndexList:
                if abs(j-i)<= k:
                    beautList.append(i)
                    break
        return beautList