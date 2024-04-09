class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:


    
        # [1,2,2]
        # i + j <= limit
        #  res.append[i,j]
        #  i+=1
        #  j-=1
        #  boat+=1
        #  else:
        #   j-=1
        
        # boat+=1
        
        n = len(people)
        people.sort()
        
        left, right =  0, n-1
        res = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left+=1
                right-=1
            else:
                right -=1
                # cant fit, Mota person, will be by himself :P
            res+=1 # each iteration 1 boat
            
        return res
