class BrowserHistory:
    # Time Complexity = O(N), Space: O(N)


    # def __init__(self, homepage: str):

    #     self.history = [homepage]
    #     self.curr_page_idx = 0 
        

    # def visit(self, url: str) -> None:

    #     if len(self.history) > self.curr_page_idx + 1:
    #         #erase history
    #         # [0,1,2,3] Len 4, curr 2/

    #         # This Takes Time: O(N), Space = O(N)
    #         self.history = self.history[:self.curr_page_idx+1]
    #     self.history.append(url)
    #     self.curr_page_idx += 1

    # def back(self, steps: int) -> str:
    #     back_step = max(self.curr_page_idx - steps, 0)
    #     self.curr_page_idx = back_step
    #     return self.history[back_step]


        

    # def forward(self, steps: int) -> str:
    #     forward_step = min(self.curr_page_idx + steps, len(self.history)-1)
    #     self.curr_page_idx = forward_step
    #     return self.history[forward_step]

    # Time complexity O(1), space O(N)
    # Two Stacks

    def __init__(self, homepage: str):
        self._history, self._future = [], []
        # 'homepage' is the first visited URL.
        self._current = homepage

    def visit(self, url: str) -> None:
        # Push 'current' in 'history' stack and mark 'url' as 'current'.
        self._history.append(self._current)
        self._current = url
        # We need to delete all entries from 'future' stack.
        self._future = []

    def back(self, steps: int) -> str:

        while steps > 0 and self._history:
            self._future.append(self._current)
            self._current = self._history.pop()
            steps-=1
        return self._current
    
    def forward(self, steps: int) -> str:

        while steps > 0 and self._future:
            self._history.append(self._current)
            self._current = self._future.pop()
            steps-=1
        return self._current



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)