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

        while curr:

            for col in range(left, right+1):
                if curr:
                    result[row][col] = curr.val
                    curr = curr.next
                else:
                    break
            
            for row in range(up+1, down+1):
                if curr:
                    result[row][col] = curr.val
                    curr = curr.next
                else:
                    break
            
            if up!=down:
                # if row up and row down are not same, then it makes sense 
                #  to L--> R
                #  or R--> L
                
                for col in range(right-1, left-1, -1):
                    if curr:
                        result[row][col] = curr.val
                        curr = curr.next
                    else:
                        break

            if left!=right:
                
                for row in range(down-1, up, -1):
                    if curr:
                        result[row][col] = curr.val
                        curr = curr.next
                    else:
                        break

            left+=1
            up+=1
            down-=1
            right-=1

        return result
        