class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count = 0
        startAttack = timeSeries[0]
        prevAttackEnd = timeSeries[0] + duration - 1 #2

        for attack in timeSeries[1:]:
            if attack <= prevAttackEnd:
                # if attack before the previous attack ends
                prevAttackEnd = attack + duration - 1
            else:
                count += prevAttackEnd - startAttack + 1
                startAttack = attack
                prevAttackEnd = attack + duration - 1
        #last value
        count += prevAttackEnd - startAttack + 1
        return count
            
