class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        nextIndex = 0
        n = len(nums)

        #reader and writer Pointer

        for runner in range(n):
            if nums[runner]!=val:
                nums[nextIndex], nums[runner] = nums[runner], nums[nextIndex]
                nextIndex+=1
        return nextIndex