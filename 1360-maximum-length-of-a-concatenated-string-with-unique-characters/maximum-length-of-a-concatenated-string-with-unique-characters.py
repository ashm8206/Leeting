class Solution:
    def maxLength(self, arr: List[str]) -> int:



        # Iterative

        # results = [""]

        # best = 0

        # for word in arr:

            
        #     for i in range(len(results)):

        #         new_res = results[i] + word

        #         if len(new_res)!= len(set(new_res)):
        #             continue
                
        #         results.append(new_res)

        #         best = max(best, len(new_res))
        # return best


        # Backtracking/ Recursion

    

        def dfs(slate, pos) -> int:      
            # Use a set to check res for duplicate characters
            if len(slate) != len(set(slate)):
                return 0

            # Recurse through each possible next option
            # and find the best answer
            best = len(slate)
            for i in range(pos, len(arr)):
                best = max(best, dfs(slate + arr[i], i+1))
            return best
        return dfs('',0)


        # Not sliding window, as it Subsequence not subarray

        # maxLen = -10**10
        # n = len(arr)
        # curr_str = ''
        # l = 0

        # for r in range(n):

        #     if len(arr[r])!= len(set(arr[r])):
        #         continue
            
            
        #     curr_str += arr[r]
        #     if len(set(curr_str))!=len(curr_str):
        #         # print(curr_str)
        #         l = l + 1
        #         curr_str = "".join(arr[l:r+1])
        #         # print(curr_str)
                
        
        #     maxLen = max(maxLen,len(curr_str))

        # return maxLen if maxLen > -10**10 else 0


