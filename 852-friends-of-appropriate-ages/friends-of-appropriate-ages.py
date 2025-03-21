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
                    ans -= countA  
                    # countA * (countA - 1) = countA*countA - countA
                    # Avoid double-counting pairs of the same age
        
        return ans