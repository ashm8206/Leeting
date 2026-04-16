class Solution:
    def compress(self, chars: List[str]) -> int:

        n = len(chars)
        left = 0
        if n == 1:
            return n

        # ["a","a","b","b","c","c","c"]
        #  .........r,l

        count = 1
        for right in range(1, n+1):
            if right < n and chars[right-1] == chars[right]:
                count+=1
            else:
                # step is imp. a....10 b a, 10 yakes 3 values
                chars[left] = chars[right-1] 
                left+=1 
                if count > 1:
                    for c in str(count):
                        chars[left] = c
                        left+=1
                count = 1 # next run
        return left
             
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        count = 1
        left = 0
        N = len(chars)
        # when we are going to the nextcahr to check in the previous char
        # we need to do the Operation for Last Char..

        # Hence N+1
        for right in range(1,N+1):
            if right < N and chars[right-1] == chars[right]:
                count += 1
            else:
                # ["a","a","a","b","b","a","a"]
                chars[left] = chars[right-1]
                left += 1
                if count > 1:
                    for c in str(count):
                        chars[left] = c
                        left += 1
                count = 1
       
        return left # +1 the index, which is what they asked for


        # slow = 0
        # n = len(chars)

        # if n==1:
        #     return 1
        

        # stack = []

        # fast = 1
        # count = 1 # one char

        # while fast < n:
        #     if chars[slow]==chars[fast]:
        #         fast+=1
        #         count+=1
        #     else:
        #         stack.append(chars[slow])

        #         if 1 < count <= 9 :
        #             stack.append(str(count))
        #         elif count > 9:
        #             count = str(count)
        #             while len(count) > 0:
        #                 stack.append(count[0]) # on repeat
        #                 count = count[1:]
        #         # print(slow, fast, stack)
        #         slow = fast
        #         fast = slow + 1
        #         count = 1

        # stack.append(chars[slow])
        # if count > 1:
        #     stack.extend(list(str(count)))

        
        # chars[:] = stack
        # return len(stack)