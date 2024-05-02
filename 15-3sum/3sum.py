class Solution:

    def twoSum(self, start,end,idx,nums):
        key = -nums[idx]
        i = start
        j = end
        res = set()
        while i < j:
            if (nums[i] + nums[j]) < key:
                i+=1
            elif (nums[i] + nums[j]) > key:
                j-=1
            else:
                res.add((nums[idx],nums[i],nums[j]))
                i+=1
                j-=1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res= []
        nums.sort()
        # print(nums)
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i-1]==nums[i]:
                continue

            result = self.twoSum(i+1,n-1,i,nums)
            # why do we pass i+1,
            # cuz it is assumed that for i-1, nums 
            # Triplets that statisfy the condition have already been found.

            if result:
                res.extend(list(result))
        return res


#Method II
# class Solution:

#     def threeSum(self, nums: List[int]) -> List[List[int]]:

#         if len(nums) < 3:
#             return []

#         if len(nums) > 3 and len(set(nums))==1 and nums[0]==0:
#             return [[0,0,0]]
        
#         results = set() # by making this a set, we can remove duplicate valid 3sum seqs presence in O(1)
#         dups = set() # records args to 2sum for duplicates
#         results_arr = [] # output format
#         for k in range(0, len(nums)): # O(n)
#             if nums[k] not in dups: # without this we fail case of [0,0,...]
#                 dups.add(nums[k])
                
#                 validSums = self.twoSum(nums, k) # get all valid 2sum sequences in O(n)
#                 for s in validSums:
#                     r = sorted([s[0], s[1], nums[k]]) # (via Timsort) O(3lg(3)) = O(1) since we always sort 3 elements.
#                     if tuple(r) not in results: # `in` operation with set() type is fast, with list() type is slow
#                         results.add(tuple(r))
#                         results_arr.append(r)

#         return results_arr
        
#     # fetch all 2sums where n_j + n_k == target
#     # n_i + n_j + n_k = 0 (problem description)
#     # n_i + n_j = - n_k (apply 2 sum function)
#     # n_i + n_j = target (within 2 sum)
#     # n_j = target - n_i (n_j is complement)
#     def twoSum(self, nums: List[int], target_index: int):
        
#         solutions = []
        
#         target = - nums[target_index]
#         complements = defaultdict(list) # complement -> index of complement (may be multiple)
#         for i in range(len(nums)):
            
#             c = target - nums[i]

#             if c in complements: # complements[c] is the index of the complementary value
#                 for index in complements[c]:
#                     # print(target,i,index)
#                     if index!=target_index and i!=target_index and i!=index:
#                         solutions.append([nums[i], nums[index]]) 
            
                
#             complements[nums[i]].append(i)
#             # print(complements) # the current number may be a future compliment
                
#         return solutions
