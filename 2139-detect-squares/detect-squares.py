class DetectSquares:

    def __init__(self):
        self.coord_freq = defaultdict(int)
        self.y_coord = defaultdict(list)
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.coord_freq[(x,y)]+=1
        self.y_coord[y].append((x,y))

    def count(self, point: List[int]) -> int:
        count = 0
        nx, ny = point[0], point[1]
        point1 = (point[0], point[1])
        if ny in self.y_coord:
            
            for x,  _ in self.y_coord[ny]:
               
                side = abs(nx - x)

                # same point
                # will cause side = 0
                if x == nx:  
                    continue

                point2 = (nx, ny + side)
                point3 =  (x, ny + side)
                # point4 =  (x, y)
                
                if ((point2 in self.coord_freq) and (point3 in self.coord_freq)):
                    count+=(self.coord_freq[point2] * 
                     self.coord_freq[point3])
            
                
                point2_ = (nx, ny - side)
                point3_ =  (x, ny - side)

                if ((point2_ in self.coord_freq) and (point3_ in self.coord_freq)):
                    count+= (self.coord_freq[point2_] * 
                     self.coord_freq[point3_])
        return count
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)