# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
        
        def backtrack(cell =(0,0), d = 0):

            visited.add(cell)
            robot.clean()

            for i in range(4):
                new_d = (d+i)%4

                nr = cell[0] + directions[new_d][0]
                nc = cell[1] + directions[new_d][1]

                if (nr,nc) not in visited and robot.move():
                    backtrack((nr,nc), new_d)
                    go_back()

                robot.turnRight()
                #

        


        # going clockwise 
        #               up, right, down, left
        # directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        visited = set()
        backtrack()
        