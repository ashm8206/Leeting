class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = sum(accounts[0]) 
        # We can initialize the above condition BCUZ
        # There is atleast 1 row 
        # even if the row has no columns --> [[]]
        # Wouldn/t matter as sum([]) --> 0
        n = len(accounts)

        for acc_idx in range(1,n):
            maxWealth=max(maxWealth, sum(accounts[acc_idx]))
        return maxWealth
        