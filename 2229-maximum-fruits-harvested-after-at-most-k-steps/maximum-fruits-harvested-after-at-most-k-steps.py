class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        start = startPos
        max_pos = max(fruits[-1][0], start + k) + 2
        prefix = [0] * max_pos

        for pos, amount in fruits:
            prefix[pos + 1] += amount

        for i in range(1, max_pos):
            prefix[i] += prefix[i - 1]

        res = 0

        for steps_left in range(k + 1):
            left = max(start - steps_left, 0)
            right = max(start + (k - 2 * steps_left), 0)
            res = max(res, prefix[right + 1] - prefix[left])

        for steps_right in range(k + 1):
            right = start + steps_right
            left = max(start - (k - 2 * steps_right), 0)
            res = max(res, prefix[right + 1] - prefix[left])

        return res
        
       



       
        