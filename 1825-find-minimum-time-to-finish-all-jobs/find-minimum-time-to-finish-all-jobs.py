class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
    

        # def is_possible(maxWork, jobs, k):
        #     pass
        #     curr_sum = 0
        #     part = 1
        #     for job in jobs:
        #         if curr_sum + job  > maxWork:
        #             part+=1
        #             curr_sum = job
        #         else:
        #             curr_sum+= job
        #     return part <= k

        # https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/solutions/1009828/simple-python-using-partition-to-k-equal-tdoo/

        jobs.sort(reverse=True) # optimization (1)

        # def is_possible(target, buckets, idx):
        #     if idx == len(jobs):
        #         return True

        #     for i in range(len(buckets)):
        #         buckets[i] += jobs[idx]
        #         if buckets[i] <= target and is_possible(target, buckets, idx+1):
        #             return True
        #         buckets[i] -= jobs[idx]
        #         if buckets[i] == 0: # optimization (2)
        #             break
        #     return False  

        def is_possible(target, buckets, idx):
            if idx==len(jobs):
                return True
            
            for i in range(len(buckets)):
                buckets[i]+=jobs[idx]
                if buckets[i] <= target and is_possible(target, buckets, idx+1):
                    return True
                
                buckets[i]-=jobs[idx]
                if buckets[i] == 0:
                    break
            return False
        
        l = max(jobs)
        # Each worker gets the exactly 1 job
        # Maxworking time will atleast be max of the jobs

        r = sum(jobs)
      
        while l < r:
            mid = (l+r)//2

            b = [0] * k

            if is_possible(mid, b, 0):
                r = mid
            # if is_possible(mid, jobs, k):
                # r = mid
            else:
                l = mid + 1
        return l

        
        # p = float('inf')
        # for t in itertools.permutations(jobs, len(jobs)):
        #     p = min(p, solve(t, k))
        # return p

