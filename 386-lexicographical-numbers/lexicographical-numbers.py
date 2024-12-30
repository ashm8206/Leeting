
class Solution:

    
    def lexicalOrder(self, n: int) -> List[int]:
        
        result = []
        @lru_cache()
        def dfs(curr_num):

            if int(curr_num) > n:
                return

            if int(curr_num) in result:
                return
            result.append(int(curr_num))

            for i in range(10):
                
                dfs(curr_num+str(i))

        for i in range(1, 10):
            dfs(str(i))

        return result

        
        
