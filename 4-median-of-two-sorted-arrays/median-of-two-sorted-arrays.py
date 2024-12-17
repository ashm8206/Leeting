class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:  
        # Using Heap to Sort 
        # Even:
            # mid2 = (n+m)//2
            # mid = mid2 - 1
        # Odd:
            # mid = (n+m)//2
        
        # Add all elements to heap
        # Pop all till i < mid
        # previous = heap Pop() : Odd
        # else previous + next //2 : ans

        # n = len(nums1)
        # m = len(nums2)
        # mid = 0
        # mid2 = 0
        # even = False

        # if (n+m)%2==0:
        #     even = True
        #     mid2 = (n+m)//2
        #     mid = mid2 - 1
        # else:
        #     mid = (n+m)//2
    
        # minHeap = []
        
        # for num in nums1:
        #     heappush(minHeap, num)
            
        
        # for num in nums2:
        #     heappush(minHeap, num)
        

        # for i in range(mid):
        #         heapq.heappop(minHeap)

        # previous = heapq.heappop(minHeap)

        # if even:
        #     nextNum = heapq.heappop(minHeap)
        #     ans = previous + nextNum
        #     ans = ans / 2
        # else:
        #     ans = previous
        
        # return ans

       
        # log(min(n, m))

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # get the smaller array in A

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True: # this is done as median is ensured

            i = (l + r) // 2  # A
            j = half - i - 2  # B #
            # (these are indexed at 0, to remove off by 1 in both arrays)

            Aleft = A[i] if i >= 0 else float("-infinity")
            #^^ r = len(A)-1 ensures A[i] doesnt go oob 
            
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
