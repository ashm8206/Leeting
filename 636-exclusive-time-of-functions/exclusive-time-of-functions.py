class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        stack = []
        ans = [0]*n

        for log in logs:
            processId, status, timestamp = log.split(':')
            if status =="start":
                stack.append((int(processId),int(timestamp)))
            else:
                processId , timestamp_start = stack.pop() 
                timeSpent = int(timestamp) - timestamp_start + 1
                ans[processId]+= timeSpent

                if stack:
                    nextProcess, _ = stack[-1]
                    ans[nextProcess] -= timeSpent
        return ans


# For each log:

# If it's a "start" log, it pushes the process ID and timestamp onto the stack.
# If it's an end log, it pops the most recent process from the stack (which should be the corresponding start log for the current process).


# When processing an end log, it:

# Calculates the time spent by this process (end timestamp - start timestamp + 1).
# Adds this time to the total time for this process in the ans array.
# If there's another process still running (on the stack), it subtracts the time spent from that parent process's total time.

                    






        # list [idx] time
        # delta  # time other processes were running
        #------------------6
        # [-4,4]
        # 0,2 1,2
            # 5-2+1 = 4
        # 0,0  0,6
            # 6 - delta + 1
            # 6-0+1 = 7-4 = 3
        # [4-4+1-1 +8,]
        # delta = 
        # 0:0, 0:2 0:5
              # 5-2+1  4 
            
            # 6-6+1  6-6-4+1
            #0: 7
            # 7-0+1 = 8
            # hmap[proess_idx]+=3


        # [4,1]
        # delta = 5
        # 0:0, 0:2 0:5
                # 5-2+1 = 4
                # 1: 6, 1:6
                # 6-6+1 = 1
                # 7-4-0+1 = 4
                
        # 0, 0 
        # result[nextProcess[id]]

        # https://leetcode.com/problems/exclusive-time-of-functions/solutions/497890/easy-to-understand-python-solution/

        result = [0]*n
        stack = []
        delta = 0
        for process in logs:
            processIdStart, status, timestamp = process.split(':')

            # print(status)

            if status == 'start':
                stack.append([processIdStart,timestamp])
            else:
                processId , timestamp_start = stack.pop() 
                # print(processIdStart,processId)
                # any process can end
                timeSpent = int(timestamp) - int(timestamp_start) + 1
                result[int(processId)] += timeSpent  # add 1 for inclusive start
                if len(stack) > 0:
                    nextProcess, _ = stack[-1]
                    result[int(nextProcess)] -= timeSpent # for this time the above process was running, so we deduct
        
        # ["0:start:0","1:start:2","1:end:5","2:start:6","0:end:6","2:end:7"]
        # This test case is indeed invalid, a function can't terminate if it's not on the top of the stack as it's not the current function being executed.
        return result

