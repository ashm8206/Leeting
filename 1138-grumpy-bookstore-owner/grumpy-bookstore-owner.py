class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        satisfiedCustomer = 0
        l = 0
        n = len(customers)
        maxUnSatisfied = 0 
        currUnSatisfied = 0

        for r in range(n):
            if grumpy[r]==1:
                currUnSatisfied += customers[r]
            else:
                satisfiedCustomer+= customers[r]
            
            if r-l+1 > minutes:
                if grumpy[l]==1:
                    currUnSatisfied -= customers[l]
                l+=1

            maxUnSatisfied = max(maxUnSatisfied, currUnSatisfied)
            
        return satisfiedCustomer +  maxUnSatisfied

        