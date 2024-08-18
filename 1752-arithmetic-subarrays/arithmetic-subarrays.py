class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # Can m ? > n 
        # 4 6 = # (3-1)/2
        # 4 9 = # 3/5
        # 3 9 = 6/3
        #  7,10 = 15/3
        # 8, 9 = Max-min/Len(Range)
        #  -12+3 /4

        def check(arr, start, end):
            minNum = min(arr)
            maxNum = max(arr)

            diff, remainder = divmod(maxNum - minNum, end - start)
            
            if remainder > 0:
                return False

            curr = minNum
            while curr < maxNum:
                if curr not in arr:
                    return False
                curr += diff
            return True

        res = []
        for start, end in zip(l,r):
            res.append(check(nums[start:end+1], start, end))
        return res



        