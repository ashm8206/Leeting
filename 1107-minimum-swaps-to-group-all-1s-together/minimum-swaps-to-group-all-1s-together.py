class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        cnt_one = max_one = 0
        left = right = 0
        n = len(data)
        # Fixed Window
        for right in range(n):
            # updating the number of 1's by adding the new element
            cnt_one += data[right]
            # right += 1
            # maintain the length of the window to ones
            if right - left + 1 > ones:
                # updating the number of 1's by removing the oldest element
                cnt_one -= data[left]
                left += 1
            # record the maximum number of 1's in the window
            max_one = max(max_one, cnt_one)
        return ones - max_one