# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    @lru_cache(maxsize=None)
    def cachedKnows(self, a, b):
        return knows(a, b)
    
    def findCelebrity(self, n: int) -> int:
        self.n = n
        celebrity_candidate = 0
        for i in range(1, n):
            if self.cachedKnows(celebrity_candidate, i):
                celebrity_candidate = i
        if self.is_celebrity(celebrity_candidate):
            return celebrity_candidate
        return -1

    def is_celebrity(self, i):
        for j in range(self.n):
            if i == j: continue
            #if Knows(i,j) = True for Any Candidate
                            # or
            # not know(j, i) anyone doesnt know candidate : Violates the condition that candidate is the Celebrity
            if self.cachedKnows(i, j) or not self.cachedKnows(j, i):
                return False
        return True

        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                # i knows j  = False if i is Candidate 
                #(j, i) == True Every one should know candidate
                if knows(i,j) or not knows(j, i):
                    #if Knows(i,j) = True for Any Candidate
                            # or
                    # not know(j, i) anyone doesnt know candidate
                    return -1


    
