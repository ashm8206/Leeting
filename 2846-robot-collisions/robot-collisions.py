class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        if len(set(directions)) == 1:
            return healths


        res = [0]*len(positions)
        wt_positions = [[healths[i],positions[i]] for i in range(len(positions))]

        # For post -processing initial indexes of positions is stored
        HMAP = { pos: i for i, pos in enumerate(positions)}


        for i, wt in enumerate(wt_positions):
            if directions[i] == 'L':
                wt_positions[i][0] *= -1

        
        wt_positions.sort(key= lambda x:x[1])

  

        stack = []
        for r, pos in wt_positions:
            while stack and r < 0 and stack[-1][0] > 0:
                # collison only occurs with pos followed by negative
                diff = r + stack[-1][0]
                if diff < 0:
                    # new robot Wins
                    stack.pop()
                    r = (abs(r)-1)*(-1) 
                    """
                    intersting piece of "decrement" has to be done on a positive value
                    """
                elif diff > 0:
                    # new robot loses, but there is a collision, so we dec stack
                    stack[-1][0] -=1
                    r = 0  
                else:
                    # Both destroy each other
                    r = 0 # dont add to stack
                    stack.pop()
            
            if r!=0: # positive or neagtive
                stack.append([r,pos])

    
        # print(stack)
        for val, pos in stack:
            res[HMAP[pos]] = val

        return [abs(val) for val in res if val!=0]



        # Post process is important
        # the health of the robots that survive the collisions, 
        # in the same order that the robots were given, 
        # i.e. final heath of robot 1 (if survived), final health of robot 2 (if survived), and so on. 
        # If there are no survivors, return an empty array.



