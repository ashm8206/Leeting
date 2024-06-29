from collections import OrderedDict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        
        # for each user store the websites they visited
        # for each user:
            # generate the  3 len subsequence patterns (combination (next number)) from their visited Website
            # update the tuple Map
            #  Maximize Score in variable
            #  update answer also
        user_map = defaultdict(list)
        
        for user, ts, site in sorted(zip(username, timestamp, website)):
            user_map[user].append((ts, site))

        pattern_score  = defaultdict(int)
        maxScore = -10**9
        ans = 0

        # for user, websitesVisited in sorted(user_map.items(), key = lambda x : x[1][0]):
            # websitesVisited = sorted(user_map[user], key = lambda x : x[0])

        for user, websitesVisited in user_map.items():
            
            n = len(websitesVisited)
            visited = set()

            # print(user,websitesVisited)

            def getPattern(slate, index):
                nonlocal ans, maxScore
                if len(slate)==3:
                    pattern = tuple(slate[:])
                    
                    if pattern not in visited:

                        visited.add(pattern)
                        pattern_score[pattern]+=1
            
                        if pattern_score[pattern] > maxScore:
                            maxScore = pattern_score[pattern]
                            ans = pattern 
                        elif pattern_score[pattern] == maxScore:
                            ans = min(ans, pattern)
                    return

                for i in range(index, n):
                    slate.append(websitesVisited[i][1])
                    getPattern(slate, i+1)
                    slate.pop()
            getPattern([],0)
        return ans