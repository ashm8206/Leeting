
class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        
        result = []
    
        def dfs(curr_num):
            
            if curr_num > n:
                return 
                
            result.append(curr_num)

            for i in range(10):
                next_num = curr_num*10 + i
                if next_num <= n:
                    dfs(next_num)
                else:
                    break

        for i in range(1, 10):
            dfs(i)
        return result

        # result = []

        # def dfs(i):

        

        # for i in range(1, 10):
        #     dfs(i)

        
        
