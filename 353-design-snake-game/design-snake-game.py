class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        
        self.snake = collections.deque([(0,0)])    # snake head is at the front
        self.snake_positions = {(0,0)}
        self.width = width
        self.height = height
        self.food = food
        self.score = 0
        # self.movement = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    def move(self, direction: str) -> int:
        
        head_x, head_y = self.snake[-1]

        match direction:
            case "U": to = (head_x-1, head_y)
            case "D": to = (head_x+1, head_y)
            case "L": to = (head_x, head_y-1)
            case "R": to = (head_x, head_y+1)
        
        next_x, next_y = to

        if not( 0 <= next_y < self.width) or not (0 <= next_x < self.height):
            return -1
        
        if (next_x, next_y) in self.snake_positions and (next_x, next_y)!=self.snake[0]:
            return -1

        # A move comes along, it is in the position of Tail
        # Head moves First
        
        # if len(self.food) > 0 and to== tuple(self.food[0]):
        #     print(self.score)
        #     self.score+=1
        #     self.food.pop(0)
        if self.score < len(self.food) and to == tuple(self.food[self.score]):
            self.score += 1
        else:
            # No food Found, Move snake tail
            # If found was found, Tail would remain as is
            # Only head moves in each case
            position = self.snake.popleft() # move Tail
            self.snake_positions.remove(position) # remove Position
            
            # Simulate to understand

        self.snake.append(to)
        self.snake_positions.add(to)
        
        return self.score
        
        






        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)