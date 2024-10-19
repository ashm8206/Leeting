class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # 1,2,3,3,4,5,

        skill.sort()
        n = len(skill)

        res = 0
        combined = skill[0] + skill[n-1]

        res += skill[0] * skill[n-1] 

        left = 1
        right = n-2

        while left < right:
            if (skill[left] + skill[right]) != combined:
                return -1
            else:
                res+= skill[left] * skill[right]
            left+=1
            right-=1
        return res
            
