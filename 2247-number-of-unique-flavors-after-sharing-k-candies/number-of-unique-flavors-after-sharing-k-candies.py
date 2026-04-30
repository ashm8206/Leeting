class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        my_flavors = Counter(candies[k:])
        max_flavors = len(my_flavors)
        for right in range(k, len(candies)):
            my_flavors[candies[right - k]] += 1
            my_flavors[candies[right]] -= 1
            if my_flavors[candies[right]] == 0:
                del my_flavors[candies[right]]
            max_flavors = max(max_flavors, len(my_flavors))

        return max_flavors