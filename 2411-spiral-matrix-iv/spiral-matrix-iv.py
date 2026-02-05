# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        result = [[-1 for j in range(n)] for i in range(m)]

        curr = head
        row, col = 0, 0
        left, up = 0, 0
        right, down = n-1, m-1

        while left <= right and up <= down:

            for col in range(left, right+1):
                if curr:
                    result[up][col] = curr.val
                    curr = curr.next
                else:
                    break
            up+=1

            for row in range(up, down+1):
                if curr:
                    result[row][right] = curr.val
                    curr = curr.next
                else:
                    break
            right-=1

            if up<=down:
                # if row up and row down are not same, then it makes sense 
                #  to L--> R
                #  or R--> L
                
                for col in range(right, left-1, -1):
                    if curr:
                        result[down][col] = curr.val
                        curr = curr.next
                    else:
                        break
                down-=1

            if left<=right:
                # up is already at right spot, -1 to include it

                for row in range(down, up-1, -1):
                    if curr:
                        result[row][left] = curr.val
                        curr = curr.next
                    else:
                        break
                left+=1

        return result
        