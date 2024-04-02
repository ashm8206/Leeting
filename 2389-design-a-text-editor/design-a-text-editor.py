# Mixture of Below Two Approaches
# 1.https://leetcode.com/problems/design-a-text-editor/solutions/4711234/py-simple-solution/
# 2. https://leetcode.com/problems/design-a-text-editor/solutions/2915730/python-3-solution-beat-95-using-stack-and-queue/

from collections import deque
class TextEditor:

    def __init__(self):
        self.left = []
        self.right = deque()

    def addText(self, text: str) -> None:
        for char in text:
            self.left.append(char)

    def deleteText(self, k: int) -> int:

        k = min(k, len(self.left))
        delCount = 0

        while k:
            self.left.pop()
            delCount+=1
            k-=1
        return delCount


    def cursorLeft(self, k: int) -> str:
        k = min(k, len(self.left))

        for i in range(k, 0, -1):
            self.right.appendleft(self.left.pop())

        curr_Left = min(10,len(self.left))

        return "".join(self.left[i] for i in range(-curr_Left, 0))
        

    def cursorRight(self, k: int) -> str:
        k = min(k, len(self.right))

        for i in range(0, k):
            self.left.append(self.right.popleft())
        
        curr_Left = min(10,len(self.left))

        return "".join(self.left[i] for i in range(-curr_Left, 0))


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)