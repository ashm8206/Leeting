class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        age_count = Counter(ages)
    
        ans = 0
        for ageA, countA in age_count.items():
            for ageB, countB in age_count.items():
                # Skip invalid conditions
                if ageA * 0.5 + 7 >= ageB or ageA < ageB or (ageA < 100 < ageB):
                    continue
                ans += countA * countB
                if ageA == ageB:
                    ans -= countA  # Avoid double-counting pairs of the same age
        
        return ans
        # count = [0] * 121
        # for age in ages:
        #     count[age] += 1

        # ans = 0
        # for ageA, countA in enumerate(count):
        #     for ageB, countB in enumerate(count):
        #         if ageA * 0.5 + 7 >= ageB: continue
        #         if ageA < ageB: continue
        #         if ageA < 100 < ageB: continue
        #         ans += countA * countB
        #         if ageA == ageB: ans -= countA

        # return ans