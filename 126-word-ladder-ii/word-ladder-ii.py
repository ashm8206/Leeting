from collections import defaultdict, deque


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> list[list[str]]:

        # 1. Create adjacency list
        def adjacencyList():

            adj = defaultdict(list)
            for word in wordList:
                for i, _ in enumerate(word):
                    pattern = word[:i] + "*" + word[i + 1 :]
                    adj[pattern].append(word)
            return adj

        # 2. Create reversed adjacency list
        def bfs(adj):

            reversedAdj = defaultdict(list)

            # Initialize the queue
            queue = deque([beginWord])

            visited = set([beginWord])

            # while q:
            #     curr_word = q.popleft()

            #     visited.add(curr_word)

            #     if curr_word == endWord:
            #         break


            #     for i in range(L):
            #         key = curr_word[:i]+"*"+curr_word[i+1:]
            #         if key in adj:
            #             for next_word in adj[key]:
            #                 reversedAdj[next_word].append(curr_word)
            #                 if next_word not in visited:
            #                     q.append(next_word)
            # return reversedAdj

            while queue:

                visitedCurrentLevel = set()
                n = len(queue)

                # Iterate through all words in Queue
                for _ in range(n):

                    
                    word = queue.popleft()
                    for i, _ in enumerate(word):

                        pattern = word[:i] + "*" + word[i + 1 :]

                        for nextWord in adj[pattern]:
                            if nextWord not in visited:

                                reversedAdj[nextWord].append(word)

                                if nextWord not in visitedCurrentLevel:

                                    # Add such word to the queue
                                    queue.append(nextWord)

                                    # Mark such word as visited
                                    visitedCurrentLevel.add(nextWord)

                # Once we done with a level, add all words visited at this level to the visited set
                visited.update(visitedCurrentLevel)

                if endWord in visited:
                    break
            return reversedAdj

            
        def dfs(reversedAdj, res, path):

            # If the first word in a path is beginWord, we have succesfully constructed a path
            if path[0] == beginWord:

                # Add such path to the result
                res.append(list(path))

                return res

            word = path[0]

            for nextWord in reversedAdj[word]:
                path.appendleft(nextWord)
                dfs(reversedAdj, res, path)
                path.popleft()
            return res

        # Do all three steps
        adj = adjacencyList()
        reversedAdj = bfs(adj)
        res = dfs(reversedAdj, [], deque([endWord]))

        return res