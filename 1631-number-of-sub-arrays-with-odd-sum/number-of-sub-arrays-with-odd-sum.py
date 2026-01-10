class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        MOD = 1e9 + 7
        n = len(arr)
        count = 0


        # chnages nothing, still have to find s, e
        # # Prefix Sum
        # prefix_sums= [0] * (n+1)
        # for i in range(n):
        #     prefix_sums[i+1] = prefix_sum[i-1] + nums[i]
        

        # # Generate all possible subarrays
        # for start_index in range(n):
        #     current_sum = 0
        #     # Iterate through each subarray starting at start_index
        #     for end_index in range(start_index, n):
        #         current_sum += arr[end_index]
        #         # Check if the sum is odd
        #         if current_sum % 2 != 0:
        #             count += 1
        # return int(count % MOD)

        odd_count = 0
        even_count = 1
        prefix_sum = 0 

        # If you have seen 3 Odd prefix sums in the past, 
        # it means there are 3 different places you could have started your subarray to      # result in an odd sum right now. So, you add 3 to your total count.

        for num in arr:
            prefix_sum += num

            if prefix_sum%2==0:
                count += odd_count
                even_count+=1
            
            else:
                count += even_count
                odd_count+=1

            count %= MOD
        return int(count)
