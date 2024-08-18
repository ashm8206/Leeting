class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        # Method I - Optimal : O(n^2), O(1) space
        def check(arr, start, end):
            minNum = min(arr)
            maxNum = max(arr)

            diff, remainder = divmod(maxNum - minNum, end - start)
            
            if remainder > 0:
                '''There is a remainder, 
                so range can't be divided equally'''
                return False
            
            #okay we got 0 remainder, 
            # so range can be divided equally, 
            #  but are this numbers present in the array ??

            "We check that below"
            curr = minNum
            while curr < maxNum:
                if curr not in arr:
                    return False
                curr += diff
            return True

        # Method II  O(n^2) / On^2logn, O(n) space
        def check(arr, start, end):
         
            temp = sorted(arr) # NlogN or N
            # print(temp)
            diff = set()
            for i in range(1, end-start+1):
                
                diff.add(temp[i]-temp[i-1])
                # print(i, diff)
                if len(diff) > 1:
                    return False
            return True

        res = []
        for start, end in zip(l,r):
            
            res.append(check(nums[start:end+1], start, end))
           
        return res



        