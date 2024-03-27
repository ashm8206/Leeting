class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # Consider Acts move through each other

        # Get max of two values
        # 1. Dist L : Diff between 0 - the Farthest ant of Left moving towards 0
        # 2. Dist R : Diff between N -  The Closest ant to 0 -- moving towards N
        leftMaxdist = abs(0-max(left)) if left else 0

        rightMindist = abs(n-min(right)) if right else 0
        return max(leftMaxdist,rightMindist)