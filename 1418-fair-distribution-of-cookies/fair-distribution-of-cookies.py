class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        def dfs(index):
            # Base case: if all cookies have been considered
            if index >= len(cookies):
                # Record the maximum cookies any child has to minimize it
                self.best_distribution = min(self.best_distribution, max(children_cookies))
                return
          
            # Iterate through each child
            for j in range(k):
                # Skip this distribution if:
                # 1. Current distribution already exceeds the best distribution found
                # 2. To avoid duplicate distributions, skip if the current child has the same number of cookies as the previous child
                if children_cookies[j] + cookies[index] >= self.best_distribution or (j > 0 and children_cookies[j] == children_cookies[j - 1]):
                    continue
              
                # Distribute current cookie to child j and recurse
                children_cookies[j] += cookies[index]
                dfs(index + 1)
                # Backtrack: remove the current cookie from child j
                children_cookies[j] -= cookies[index]
      
        # Initialize best distribution as infinity
        self.best_distribution = float('inf')
        # Initialize list to keep track of cookies each child has
        children_cookies = [0] * k
        # Sort cookies in descending order to distribute larger cookies first
        cookies.sort(reverse=True)
        # Start recursive distribution
        dfs(0)
        # Return the minimum of the maximum number of cookies any child has
        return self.best_distribution


            
            
