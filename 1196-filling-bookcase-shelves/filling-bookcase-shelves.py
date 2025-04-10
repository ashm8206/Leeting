class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        # @lru_cache(maxsize=None) # 1. Simple Caches
        # memo = {} # 2. Top Down

        # def place(idx):
        #     if idx ==n:
        #         return 0
            
        #     if idx in memo:
        #         return memo[idx]
            
        #     curr_width = 0
        #     curr_max_height = 0
        #     min_shelf_ht = float("inf")
        #     for j in range(idx, n):
        #         w, h = books[j]
        #         curr_width+= w

        #         if curr_width > shelfWidth:
        #             break
                
        #         curr_max_height = max(curr_max_height, h)
        #         total_ht_choice =  curr_max_height + place(j+1)
        #         min_shelf_ht = min(min_shelf_ht, total_ht_choice)
        #     # return min_shelf_ht
        #     memo[idx] = min_shelf_ht
        #     return memo[idx]
        # return place(0)

        # Bottom Up

        dp = [float('inf')] * (n + 1)
        dp[n] = 0  # Base case: no books left = 0 height

        for i in range(n-1, -1, -1):
            curr_width = 0
            curr_max_height = 0
            for j in range(i, n):
                w, h = books[j]
                if curr_width + w > shelfWidth:
                    break
                curr_width+=w  
                curr_max_height = max(curr_max_height, h)
                total_ht_choice =  curr_max_height + dp[j+1]
                dp[i] = min(dp[i], total_ht_choice)
        return dp[0]


