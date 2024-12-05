class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        n = len(start)
        start_idx = 0
        target_idx = 0

        # if ( start.count("L")!=target.count("L") 
        # or start.count("R")!=target.count("R")):
        #     return False



        while start_idx < n or target_idx < n:
        
            while start_idx < n and start[start_idx] == '_':
                start_idx+=1
       

            while target_idx < n and target[target_idx] == '_':
                target_idx+=1
            
            
            # if one exahusts, both have to exhaust

            # why? 
            #  Each iteration we are matching every no-blank pair

            # if there are more L / R in one string, 
            # One will exhaust before the other

            #  if startL=targetL and startR=targetR
            #  even in case of All blanks, i.e 0 Ls and Rs
            # "__" == "__" They will exhaust together!!
            
            if start_idx == n or target_idx==n:
                # print(start_idx, target_idx)
                return (start_idx==n and target_idx==n)
         
            

            # check is positions are valid and if the chars match

            # RL__ , __LR

            if (start[start_idx]!=target[target_idx] 
                or target[target_idx]=="L" and start_idx < target_idx
                or target[target_idx]=="R" and target_idx < start_idx 
                ): 
                
                return False
            else:
                start_idx  +=1
                target_idx +=1
        return True
    
        