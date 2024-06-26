class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair =[ (pos,v) for pos, v in zip(position,speed)]

        pair.sort(key = lambda x : x[0])

        n = len(pair)

        stack = []

        for pos, v in pair:

            dist = target - pos
            t = dist/ v

            while stack and stack[-1] <= t:
                stack.pop()
            
            stack.append(t)

        return len(stack)

        # pos   # 0, 2, 4
        # time  # 25, 49, 96 
        #  car at 0 will reach in 25 seconds, since its a single road 
        #  it will collide with the next cars to form a fleet if 
        #  currentCar <= nextCarTime
        #      # Pop the result

