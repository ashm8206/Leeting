from collections import OrderedDict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        # Hint : 
        
        # for each user store the websites they visited in order of least TS

        # for each user:
            # generate the  3 len subsequence/subset patterns 

            

        user_map = defaultdict(list)
        
        # for user, ts, site in sorted(zip(username, timestamp, website)):
        #     user_map[user].append((ts, site))

        for user, ts, site in sorted(zip(username, timestamp, website)):
            user_map[user].append((site, ts))

        


        pattern_score  = defaultdict(int)
        maxScore = -10**9
        ans = tuple()

   

        for user, websitesVisited in user_map.items():
            
            n = len(websitesVisited)
            UserPatternVisited = set()
            # If a user Visits the same pattern a 2nd time
            # it is only counted towards his score once

            def getPattern(idx, slate):
                nonlocal ans, maxScore
                if len(slate) == 3:
                    # we found the pattern
                    pattern = tuple(slate[:])

                    if pattern not in UserPatternVisited:
                        UserPatternVisited.add(pattern)
                        pattern_score[pattern]+=1

                        if pattern_score[pattern] > maxScore:
                                maxScore = pattern_score[pattern]
                                ans = pattern 
                        elif pattern_score[pattern] == maxScore:
                                ans = min(ans, pattern)
                        
                    return
                

                for end in range(idx, n):
                    slate.append(websitesVisited[end][0])
                    getPattern(end+1, slate)
                    slate.pop()


            getPattern(0,[])
        return list(ans)

    



            
        # return ans




        # def getPattern(slate, index):
        #         nonlocal ans, maxScore
        #         if len(slate)==3:
        #             pattern = tuple(slate[:])
                    
        #             if pattern not in visited:

        #                 visited.add(pattern)
        #                 pattern_score[pattern]+=1
            
        #                 if pattern_score[pattern] > maxScore:
        #                     maxScore = pattern_score[pattern]
        #                     ans = pattern 
        #                 elif pattern_score[pattern] == maxScore:
        #                     ans = min(ans, pattern)
        #             return

        #         for i in range(index, n):
        #             slate.append(websitesVisited[i][1])
        #             getPattern(slate, i+1)
        #             slate.pop()
        #     getPattern([],0)