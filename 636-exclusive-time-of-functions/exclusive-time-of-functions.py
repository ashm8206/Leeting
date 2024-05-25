class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
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
                print(processIdStart,processId)
                # any process can end
                timeSpent = int(timestamp) - int(timestamp_start) + 1
                result[int(processId)] += timeSpent  # add 1 for inclusive start
                if len(stack) > 0:
                    nextProcess, _ = stack[-1]
                    result[int(nextProcess)] -= timeSpent # for this time the above process was running, so we deduct
        
        # ["0:start:0","1:start:2","1:end:5","2:start:6","0:end:6","2:end:7"]
        # This test case is indeed invalid, a function can't terminate if it's not on the top of the stack as it's not the current function being executed.
        return result

