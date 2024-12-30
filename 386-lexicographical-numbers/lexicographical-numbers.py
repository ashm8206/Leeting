
class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        
        # result = []
    
        # def dfs(curr_num):
        #     if curr_num > n:  
        #         # for singal digit numbers, execeeding limit
        #         #  limit is 2, but Outer loop is [1.....10]
        #         return 

        #     result.append(curr_num)

        #     for i in range(10):
        #         next_num = curr_num*10 + i

        #         if next_num <= n:
        #             dfs(next_num)
        #         else:
        #             return 

        # for i in range(1, 10): 
        #     # this optimization
        #     dfs(i)
        # return result


        # Iterative Neetcode
        
        res = []
        curr = 1

        while len(res) < n:
            res.append(curr)

            if curr * 10 <= n:
                curr *= 10
            else:

                while curr == n or curr%10==9:
                    curr //= 10
                curr+=1
        return res
       
        

       

        
        
