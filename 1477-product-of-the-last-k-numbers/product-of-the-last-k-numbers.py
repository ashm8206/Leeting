class ProductOfNumbers:

    def __init__(self):
        self.stream = [1]
        self.len = 0
    def add(self, num: int) -> None:
        if num == 0:
            self.stream = [1]
            self.len = 0
        else:
            self.stream.append(self.stream[self.len] * num)
            self.len+=1

    def getProduct(self, k: int) -> int:
        if k > self.len:
            return 0
        return self.stream[self.len] // self.stream[self.len - k]  
        # k==self.len == stream[0] ==1
         
      



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)