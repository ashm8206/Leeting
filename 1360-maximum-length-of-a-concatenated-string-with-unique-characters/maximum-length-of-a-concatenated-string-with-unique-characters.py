class Solution:
    def maxLength(self, arr: List[str]) -> int:



        # Recursion/ Bactarcking

        results = [""]

        best = 0

        for word in arr:

            
            for i in range(len(results)):

                new_res = results[i] + word

                if len(new_res)!= len(set(new_res)):
                    continue
                
                results.append(new_res)

                best = max(best, len(new_res))
        return best


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


