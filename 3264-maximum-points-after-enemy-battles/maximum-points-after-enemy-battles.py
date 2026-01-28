class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        minEnergy = min(enemyEnergies)

        if minEnergy > currentEnergy:
            return 0 # we dont get the first pt

        currentEnergy += sum(enemyEnergies) - minEnergy
        # saying the enmey with minEnergy is left unmarked

        # now point is 
        return currentEnergy // minEnergy