class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(profit, difficulty), reverse = True)
        worker.sort(reverse=True)
        j = 0
        i = 0


        n = len(jobs)
        num_worker =  len(worker)

        total_profit = 0

        while i < n:
            if j <  num_worker:
                if jobs[i][1] > worker[j]:
                    # move to lower diffciulty
                    i+=1
                else:
                    total_profit += jobs[i][0] 
                    j+=1
                    # keep the job ptr here
            else:
                return total_profit
        # return total_profit




        # maxprofit, difficulty : 
        # 99,57 : 
        # 66,47
        # 24,85

        # 40, 25, 25
        
      
        res = i = best = 0

        for ability in sorted(worker, reverse=True):
            best = 0
            while i < len(jobs):
                if ability >= jobs[i][1]:
                    best = jobs[i][0]
                    break
                i += 1
            #print(ability,best)
            res += best
        return res
        
