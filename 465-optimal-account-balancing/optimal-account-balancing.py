class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance_map = collections.defaultdict(int)
        for a, b, amount in transactions:
            balance_map[a] += amount # debt he owes
            balance_map[b] -= amount
        
        balance_list = [amount for amount in balance_map.values() if amount]
        
        n = len(balance_list)
        
        def dfs(cur):
            # Skip Zero balance
            while cur < n and balance_list[cur]==0:
                cur += 1
             # Work Done
            if cur == n:
                return 0
            cost = float('inf')
            for nxt in range(cur + 1, n):
                # If nxt is creditor and curr is debitor : valid transaction
                #    Check with their Prod < 0
                # 1. add cur's balance to nxt.
                # 2. recursively call dfs(cur + 1).
                # 3. remove cur's balance from nxt.
                if balance_list[nxt] * balance_list[cur] < 0:
                    balance_list[nxt] += balance_list[cur]
                    # the debt of cur is added to the balance 
                    cost = min(cost, 1 + dfs(cur + 1))
                    balance_list[nxt] -= balance_list[cur]
            return cost
        
        return dfs(0)