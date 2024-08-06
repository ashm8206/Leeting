class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #  10 , -5
        #  -5, 10
        #  10, -11
        #  10, 10

        # store all positive asteroids and the negative asteroids case  by case basis
        #  to pass through the positive asterioids barrier

        # https://www.youtube.com/watch?v=LN7KjRszjk4&t=706s
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                # collison only occurs with pos followed by negative
                diff = a + stack[-1]
                if diff < 0: 
                    # new asteriod Wins
                    stack.pop()
                elif diff > 0:
                    a = 0  # do nothing, come cout of loop
                else:
                    # Both destroy each other
                    a = 0 # dont add to stack
                    stack.pop()
            
            if a!=0: # positive or neagtive
                stack.append(a)

        return stack
        
   