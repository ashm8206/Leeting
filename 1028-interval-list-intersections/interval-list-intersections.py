class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        lenA = len(firstList)
        lenB = len(secondList)

        A = firstList
        B = secondList

        start, end = 0,1
        currA, currB = 0, 0

        result = []
        
        if lenA == 0 or lenB == 0:
            return result

        while currA < lenA and currB < lenB:

            # Is Overlap ?
            # max(start), min(end) 
            # last meeting to start. has not end before the first meeting to end
            
            new_start = max(A[currA][start],B[currB][start])
            new_end = min(A[currA][end],B[currB][end]) 

            if new_start <= new_end:
                result.append([new_start,new_end])
            # https://www.piratekingdom.com/leetcode/tricks/is-overlap
            
            # Since intervals are pairwise disjoint
            # [1,5], [2,6] --> Wrong testcase since they both overlap in B
            # [1,5], [6,10] --> Good Test case, since values need to be strictly increasing

            if A[currA][end] < B[currB][end]:
                # increment the smaller endpt 
                # as it has wont intersect any further
                currA+=1
            else:
                currB+=1
        return result
        
        
