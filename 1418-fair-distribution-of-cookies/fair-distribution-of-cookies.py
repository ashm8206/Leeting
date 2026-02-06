class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        
        # def is_possible(unfairness, cookies, k):
            
        #     curr_sum = 0
        #     part = 1
        #     for bag in cookies:
        #         if curr_sum + bag  > unfairness:
        #             part+=1
        #             curr_sum = bag
        #         else:
        #             curr_sum+= bag
        #     return part <= k

        
        # def solve(cookies, k):

        def is_possible(unfairness, buckets, idx):

            if idx ==len(cookies):
                return True # all cookies destributed
            
            for i in range(len(buckets)):
                buckets[i]+= cookies[idx]

                if buckets[i] <= unfairness and is_possible(unfairness, buckets, idx+1):
                    return True

                buckets[i]-= cookies[idx]

                if buckets[i] == 0:
                    break
            return False

        l = max(cookies)
        r = sum(cookies)

        while l < r:
            mid = (l+r)//2
            buckets = [0]* k
            if is_possible(mid, buckets, 0):
            # if is_possible(mid, cookies, k):
                r = mid
            else:
                l = mid + 1
        return l

        # In grouping order matters
        # p = float('inf')
        # for t in itertools.permutations(cookies, len(cookies)):
        #     p = min(p, solve(t, k))
        # return p


        # n = len(cookies)
        # childcookies = [0]*k
        # minScore = float("inf")
        # # # Sort cookies in descending order to distribute larger cookies first
        # cookies.sort(reverse=True)

        
        # def dfs(idx, curr_max):
        #     nonlocal minScore
        #     if idx == n:
        #         minScore = min(minScore, curr_max)
        #         return
        

        #     for i in range(k):
        #         childcookies[i]+= cookies[idx]
        #         dfs(idx+1, max(childcookies[i], curr_max))
        #         childcookies[i]-= cookies[idx]
        # dfs(0, 0)
        # return minScore
            

        # def dfs(index):
        #     # Base case: if all cookies have been considered
        #     if index >= len(cookies):
        #         # Record the maximum cookies any child has to minimize it
        #         self.best_distribution = min(self.best_distribution, max(children_cookies))
        #         return
          
        #     # Iterate through each child
        #     for j in range(k):
        #         # Skip this distribution if:
        #         # 1. Current distribution already exceeds the best distribution found
        #         # 2. To avoid duplicate distributions, skip if the current child has the same number of cookies as the previous child
        #         if children_cookies[j] + cookies[index] >= self.best_distribution or (j > 0 and children_cookies[j] == children_cookies[j - 1]):
        #             continue
              
        #         # Distribute current cookie to child j and recurse
        #         children_cookies[j] += cookies[index]
        #         dfs(index + 1)
        #         # Backtrack: remove the current cookie from child j
        #         children_cookies[j] -= cookies[index]
      
        # # Initialize best distribution as infinity
        # self.best_distribution = float('inf')
        # # Initialize list to keep track of cookies each child has
        # children_cookies = [0] * k
        # # Sort cookies in descending order to distribute larger cookies first
        # cookies.sort(reverse=True)
        # # Start recursive distribution
        # dfs(0)
        # # Return the minimum of the maximum number of cookies any child has
        # return self.best_distribution


            
            
