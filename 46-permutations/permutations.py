class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(slate,arr):
            if not arr:
                res.append(slate[:])
                return
            
            for i, num in enumerate(arr):
                slate.append(num)
                backtrack(slate, arr[:i]+arr[i+1:])
                slate.pop()
        backtrack([],nums)
        return res

        # def backtrack(slate):
        #     if len(slate) == n:
        #         # we  only append when len(slate) == n
        #         res.append(slate[:])
        #         return

        #     for i in range(0,n):
        #         # start point is all numbers
        #         # This is different from subset,
        #         #  each next iteration only cares bout [ i.. n]
        #         #  pick or not pick at each i

        #         # Wheras for permuation
        #         # we get to choose from all [:i] [i+1: ]
        #         #  constraint of not choosing same [i] again

        #         if nums[i] in slate:
        #             continue
        #         #else
        #         slate.append(nums[i])
        #         backtrack(slate)
        #         slate.pop()
        # backtrack([])
        # return res
            



        #     # for i in range(first, n):
        #     #     nums[i], nums[first] = nums[first], nums[i]
        #     #     backtrack(first + 1)
        #     #     #They are swapped, i.e  i==first and first==i so we swap back
        #     #     nums[i], nums[first] = nums[first], nums[i]
        #     #     #nums[i], nums[first] = nums[i], nums[first]
        # # if nums:
        