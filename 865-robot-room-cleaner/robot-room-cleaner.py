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

        # Right hand rule /Maze solving algo, where you cant see the the board 
        #  if You cant see the board, and obstacle TURN RIGHT
        #  visited cells are Obstacles 

        def go_back():
            # R ---> facing down
            # Turn Right  --> faces next right cell
            # Turn Right --> faces up
            #  Move    cell in front, is one cell up
            #  Turn Left --> faces next left cell
            # Turn left --> faces next down cell

            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
        
        def backtrack(cell =(0,0), d = 0):

            visited.add(cell)
            robot.clean()

            for i in range(4):
                # Stop when you explored all possible paths, 
                # i.e. all 4 directions (up, right, down, and left) for each visited cell.
                new_d = (d+i)%4

                nr = cell[0] + directions[new_d][0]
                nc = cell[1] + directions[new_d][1]

                if (nr,nc) not in visited and robot.move():
                    backtrack((nr,nc), new_d)
                    go_back()

                robot.turnRight()
                #  you explore Up first, fron nr,nc
                #  explore the next cell in clockwise direction

        # going clockwise 
        #               up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        # the order of directions dont matter
        visited = set()
        backtrack()
        