class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]
        n = len(folder)

        for i in range(1, n):
            last_folder = res[-1]
            last_folder+= '/'

            if not folder[i].startswith(last_folder):
                res.append(folder[i])
            
        return res

            
            