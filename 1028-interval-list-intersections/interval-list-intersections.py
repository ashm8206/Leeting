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
            
            new_start = max(A[currA][start],B[currB][start])
            new_end = min(A[currA][end],B[currB][end]) 
            if new_start <= new_end:
                result.append([new_start,new_end])

            
            if A[currA][end] < B[currB][end]:
                currA+=1
            else:
                currB+=1
        return result

        # 0  2  5 10  13 23
        #   1   5
        # Is Overlap ?
        # max(start), min(end) 
        # last meeting to start. has not end before the first meeting to end
        
