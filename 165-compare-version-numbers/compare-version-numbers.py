class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int,version1.split(".")))
        version2 = list(map(int,version2.split(".")))

        n1 = len(version1)
        n2 = len(version2)
        reversed_flag = False
        if n2 > n1:
            version1, version2 = version2, version1
            n1, n2 = n2, n1
            reversed_flag = True

        
        for i in range(n1):
            version1_val = version1[i]
            version2_val = version2[i] if i < n2 else 0
            
            if version1_val == version2_val:
                continue

            if version1_val > version2_val:
                return -1 if reversed_flag else 1
            else:
                return 1 if reversed_flag else -1
        return 0