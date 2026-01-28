from collections import OrderedDict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        # Hint : 
        # 1.We must sort and Store pattern visits in asce time
        #   This is Important to make ordered visits

        #2. If a user visited the same pattern twice, he contributes only 1 to the score of the pattern
       

        
        # for each user store the websites they visited in order of least TS

        # for each user:
            # generate the  3 len subsequence/subset patterns 
            # When pattern found
            #.  update current_pattern_score,  update maxscore and ans
        

            

        user_map = defaultdict(list)
        
        for user, ts, site in sorted(zip(username, timestamp, website)):
            user_map[user].append((ts, site))

    
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
                    slate.append(websitesVisited[end][1])
                    getPattern(end+1, slate)
                    slate.pop()


            getPattern(0,[])
        return list(ans)



