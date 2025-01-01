class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # https://www.youtube.com/watch?v=giomYhFJo6g
        dp = {}
        def helper(left,right, turn):
            if left > right:
                return 0
            
            if (left,right, turn) in dp:
                return dp[(left,right, turn)]

            res = 0
            if turn ==1:
                res = max(nums[left]+ helper(left+1,right,2), nums[right]+ helper(left,right-1,2))
            else:
                # turn 2
                # we want to try and minimize turn 1 score above where its added
                # so mininum is returned

                res = min(helper(left+1,right,1), helper(left,right-1,1))
            dp[(left,right, turn)] = res
            return res

        n = len(nums)
        p1_score = helper(0,n-1, 1)
        p2_score = sum(nums) - p1_score
        return p2_score <= p1_score
          