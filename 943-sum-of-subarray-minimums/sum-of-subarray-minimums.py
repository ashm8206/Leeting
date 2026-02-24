import copy
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        MOD = 10 ** 9 + 7
        stack = []
        sum_of_minimums = 0
        A = arr
        A = [0]+A
        result = [0]*len(A)
        stack = [0]
        for i in range(len(A)):
            while A[stack[-1]] > A[i]:
                stack.pop() 
            j = stack[-1]
            result[i] = result[j] + (i-j)*A[i]
            stack.append(i)
        return sum(result) % (10**9+7)
        
        # for i in range(len(arr)+[0]):  
        #     # for last number count n as nextSmallest
            
        #     while stack and arr[stack[-1]] >= arr[i]):

        #         # Notice the sign ">=", This ensures that no contribution
        #         # is counted twice. right_boundary takes equal or smaller 
        #         # elements into account while left_boundary takes only the
        #         # strictly smaller elements into account

        #         mid = stack.pop()
        #         # for mid, nextSmaller is at -i
        #         # previousSamller is at stack[-1]

        #         right_boundary = i 
        #         left_boundary = -1 if not stack else stack[-1]
                

        #         # count of subarrays where mid is the minimum element
        #         # Don't count the left or right boundary element
                
        #         count = (mid - left_boundary) * (right_boundary - mid)
        #         sum_of_minimums += (count * arr[mid])

        #     stack.append(i)
        # return sum_of_minimums % MOD

