class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n = len(arr)
        # Method I
        # n = len(arr)
        # prefix_sum = [0]* n
        # for i in range(n):
        #     prefix_sum[i] = arr[i] + (prefix_sum[i-1] if i > 0 else 0)

        # result = 0

        # for s in range(n):
        #     for e in range(s+1,n):
        #         if (e-s+1)%2==1:
        #             result+= prefix_sum[e] - (prefix_sum[s-1] if s > 0 else 0)
        # print(prefix_sum)
        # result+= prefix_sum[n-1]
        # return result


        # Total Subarray 'i' = # Subarray Ending at i  x (AND)   # Subarray starting at i  

        # 1. Ending @ i = i+1
        # 2. Starting @ i = n - i

        # Odd len subrray will be half of each End and Start values
        # if any time 1 * 2 is odd value  add +1 to odd len
        
        # for eg. [1,2,3,4]
        # [1,2,3], [2,3], [3] # 3 Total subarrays end here. How many are odd len ? 2 odd len and 1 even len,
        # hence for odd number of subrrays we add + 1:
        # We round up.


        # for num each index 
            # find number of odd_len subarray it is part of : k
            # result += nums[i]*k
        # return result

        result = 0
        for i in range(n):
            num_sub_ending = i+1
            num_sub_starting = (n-i)
            
            total_subarray = (i+1) * (n-i)

            if total_subarray%2:
                odd_subarray= (total_subarray)// 2 + 1
            else:
                odd_subarray = total_subarray // 2

            result += arr[i]*(odd_subarray)
        return result

        # TC: O(N)  https://www.youtube.com/watch?v=J5IIH35EBVE