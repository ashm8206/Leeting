class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # Method I O(N^2) 
        # n = len(gas)
        # for start in range(n):
        #     curr_petrol = 0

        #     end = start
        #     while True:
        #         curr_petrol += gas[end] - cost[end]

        #         if curr_petrol < 0:
        #             break
        #         end = (end+1) % n
        #         if end == start:
        #             return start
        # return -1

        # O(N)
        n = len(gas)
        curr_petrol = 0
        prev_petrol  = 0
        start = 0
        for i in range(n):
            curr_petrol += gas[i] - cost[i]
            if curr_petrol < 0:
                prev_petrol += curr_petrol
                start = i+1
                curr_petrol = 0
        
        return start if curr_petrol + prev_petrol >=0 else -1