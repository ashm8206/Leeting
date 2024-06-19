class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []
        n = len(s)

        def backtrack(slate, curr_idx):
            
            if len(slate) > 4:
                return 
           
            if len(slate)==4 and curr_idx == n:
                # has reached the end, and accounted for every pair in 1 RUN
                # there must be  exactly 4 elements to join to make up the IP
                res.append(".".join(slate[:]))
                return


            for win in range(1, 4):
                
                if curr_idx + win > n:
                    ""+"1"
                    ""+"11"
                    ""+ "111"
                    # important point in choices
                    break
                
                window = s[curr_idx : curr_idx+win]

                # Two constraints
                #  1. Shouldnt start with "0" if len(window) > 1
                #  2. should not be greater than 255
                
                if (len(window) > 1 and  window.startswith("0")) or  int(window) > 255:
                    continue
               
                slate.append(window)
                backtrack(slate, curr_idx+win)
                slate.pop()

        backtrack([], 0)
        return res