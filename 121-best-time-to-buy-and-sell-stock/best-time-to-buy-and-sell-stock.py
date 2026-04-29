class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minPrice = float("inf")
        ans = float("-inf")
        for j in range(1, n):
            minPrice = min(minPrice, prices[j-1])
            ans = max(prices[j] - minPrice, ans)
        return ans if ans > 0 else 0

        # different day in the future
        # minPrice = float("inf")
        # ans = float("-inf")
        # for j in range(1,n):
        #     minPrice = min(minPrice,prices[j-1]) # prices[j-1]
        #     ans = max(ans, prices[j] - minPrice)
        # return ans if ans > 0 else 0
        


        # FB  variant
        # two arrs: same size
        # min cost = returns[j] + mindep[0...j-1]
        # def FindCheapestTickets(departures,returns):
            # n = len(departures)
            # cant be same day
            # minPrice = float("inf")
            # ans = float("inf")
            # for j in range(1,n):
            #     minPrice = min(minPrice,departures[j-1])
            #     ans = min(ans, returns[j] + minPrice)
            # return ans


        #     departures = [1, 3, 10, 9, 3]
        #     returns = [1, 1, 6, 7, 10]
        #     print(FindCheapestTickets(departures, returns))
        #     assert(2 == FindCheapestTickets(departures, returns))

        #     departures = [1, 3, 10, 9, 3]
        #     returns = [10, 9, 8, 7, 6]
        #     print(FindCheapestTickets(departures, returns))
        #     assert(7 == FindCheapestTickets(departures, returns))

        #     departures = [12, 33, 44, 9, 23]
        #     returns = [100, 90, 80, 70, 15]
        #     print(FindCheapestTickets(departures, returns))
        #     assert(24 == FindCheapestTickets(departures, returns))

        #     departures = [4, 3, 5, 11, 2]
        #     returns = [1, 6, 10, 2, 9]
        #     print(FindCheapestTickets(departures, returns))
        #     assert(5 == FindCheapestTickets(departures, returns))
