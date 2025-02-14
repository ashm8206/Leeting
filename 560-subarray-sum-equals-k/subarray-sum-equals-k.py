class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {0: 1}
        count = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            # sum1 ... sum2==[sum2-sum1 = k]
            # sum2 - k = sum1
            
            count += hmap.get(diff,0)
            hmap[curr_sum] = hmap.get(curr_sum,0) + 1
        return count


    
        
        
        
        
        
        
        hmap = {0: 1}
        count = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            diff =  curr_sum - k
            
            if diff in hmap:
                count +=  hmap.get(diff, 0)
            hmap[curr_sum] = hmap.get(curr_sum, 0)  + 1
        return count


        
        # n = len(nums)
        # res = 0
        # Worst case is O(n^3)
        # 1 outer start index of subarray
        #    1 inner end index of subarray
        #       1 more inner to sum(i:j) [0.1]
                                        #  [0..2]
                                        #  [0...3]
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         curr_sum = 0
        #         # print(i,j)
        #         for x in range(i, j):
                    
        #             curr_sum +=nums[x]
        #         if curr_sum == k:
        #                 res+=1
        # return res
        #--------------------------------------------------
        # Prefix sum Trick to find Sum Between all ranges  O(N) 
        # sum[j+1] - sum[i] = uptil jth index

        # prefixSum = [0]*(n+1) # n+1 becuz sum[0] = 0  sum uptil 
        # sum[1] = sum[1] - sum[0] # sum uptil 0 in main array 

        # for i in range(1,n+1):
        #     prefixSum[i] = prefixSum[i-1] + nums[i-1]
        
        # for i in range(0, n):
        #     for j in range(i+1,n+1):
        #         # print(i,j)
        #         if(prefixSum[j]-prefixSum[i]) == k:
        #             res+=1
        # return res

        #Optimze with hashmap the Two sum 
        #prefixSum[j:::soFar]-k) == prefix_sum[i:::previous]

        # The number of the times the previous sum has occured that many times we can form the array

        #  Most Optimized
        
        hmap = {0:1} # hmap of prefix sum seen so sofar, with their counts
        curr_sum = 0
        diff = 0 # two sum
        
        for i in range(n):
            curr_sum += nums[i]
            diff = curr_sum-k
            
            res += hmap.get(diff,0) # number of times it occured before
            
            hmap[curr_sum] = hmap.get(curr_sum, 0) + 1
        
        return res
        # Intution for Brute Force Solution
        # https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/prefix_sum

        # Neetcode https://www.youtube.com/watch?v=fFVZt-6sgyo



        # Subarrat Sum equals K
        # 3 Concepts
        # 1. Two Sum
        # 2. Number of Good Pairs hmaps[key]: Counts
        # 3. Sum[i] == Sum[j] then Sum[j]-sum[i] = 0   or equal to K
