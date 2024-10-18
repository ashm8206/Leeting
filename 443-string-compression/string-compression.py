class Solution:
    def compress(self, chars: List[str]) -> int:
        slow = 0
        n = len(chars)

        if n==1:
            return 1
        

        stack = []

        fast = 1
        count = 1 # one char

        while fast < n:
            if chars[slow]==chars[fast]:
                fast+=1
                count+=1
            else:
                stack.append(chars[slow])

                if 1 < count <= 9 :
                    stack.append(str(count))
                elif count > 9:
                    count = str(count)
                    while len(count) > 0:
                        stack.append(count[0]) # on repeat
                        count = count[1:]
                # print(slow, fast, stack)
                slow = fast
                fast = slow + 1
                count = 1

        stack.append(chars[slow])
        if count > 1:
            stack.extend(list(str(count)))

        
        chars[:] = stack
        return len(stack)