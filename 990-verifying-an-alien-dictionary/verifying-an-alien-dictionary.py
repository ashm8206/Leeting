class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        custom = { key:idx for idx, key in enumerate(order)}

        # print("".join(sorted(words, key = lambda k: custom.get(k,-1))))
        # return "".join(sorted(words, key = lambda k: custom.get(k,-1)))

        # check pair of words
        # check first pair of non-match char for order
        # if they are not ordered, Break and return true

        n = len(words)
        for i  in range(1,n):
            prev = words[i-1]
            curr = words[i]

            for j in range(len(prev)):
                if j < len(curr):
                    if prev[j]!=curr[j] and custom[prev[j]] < custom[curr[j]]:
                        # first greater > element 
                        #  no need to match further break
                        break
                    else:
                        if prev[j]!=curr[j] and custom[prev[j]] > custom[curr[j]]:
                            return False
                    # print(prev[j],curr[j], j)
                if j >= len(curr):
                    return False

        return True

