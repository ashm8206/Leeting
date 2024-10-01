class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
    # Method I - complex

    #     self.memo = set()
    #     target = stones[-1]

    #     stones = set(stones) # image a pnds with stones at same possible
    #     # we can take any position

    #     res = self.bt(stones, 1,1,target)

    #     return res

    # def bt(self, stones, currPos, preJump, target):

    #     if (currPos,preJump) in self.memo:
    #         return False # visiting same stone again
        
    #     if currPos == target:
    #         return True
        
    #     if currPos > target or currPos < 0 or preJump<=0 or currPos not in stones:
    #         return False
        
    #     candidates = [preJump-1,preJump,preJump+1]

    #     for c in candidates:
    #         if (currPos + c) in stones:
    #             if self.bt(stones, currPos+c, c, target):
    #                 return True
        
    #     self.memo.add((currPos, preJump))

    #     return False

        stone_set, fail = set(stones), set()
        stack = [(0, 0)]
        while stack:
            stone, jump = stack.pop()
            for j in (jump-1, jump, jump+1):
                s = stone + j
                if j > 0 and s in stone_set and (s, j) not in fail:
                    if s == stones[-1]:
                        return True
                    stack.append((s, j))
            fail.add((stone, jump))
        return False


