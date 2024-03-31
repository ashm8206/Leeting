class BrowserHistory:

    def __init__(self, homepage: str):

        self.history = [homepage]
        self.curr_page_idx = 0 
        

    def visit(self, url: str) -> None:

        if len(self.history) > self.curr_page_idx + 1:
            #erase history
            # [0,1,2,3] Len 4, curr 2/
            self.history = self.history[:self.curr_page_idx+1]
        self.history.append(url)
        self.curr_page_idx += 1

    def back(self, steps: int) -> str:
        back_step = max(self.curr_page_idx - steps, 0)
        self.curr_page_idx = back_step
        return self.history[back_step]


        

    def forward(self, steps: int) -> str:
        forward_step = min(self.curr_page_idx + steps, len(self.history)-1)
        self.curr_page_idx = forward_step
        return self.history[forward_step]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)