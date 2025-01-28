from collections import defaultdict, deque


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> list[list[str]]:

        wordDict = defaultdict(set)

        for word in wordList:
            # if word != beginWord:
                for i in range(len(word)):
                        wordDict[word[:i] + "*" + word[i+1:]].add(word)
        queue = deque([beginWord])
        visited = {beginWord: 1}
        parent_list = defaultdict(set)
        ans_path = []
        # print(wordDict)
        
        while queue:
            word = queue.popleft()
            if word == endWord:             
                break
            for i in range(len(word)):
                for next_word in wordDict[word[:i] + "*" + word[i+1:]]:
                    if next_word not in visited:
                        visited[next_word] = visited[word] + 1
                        queue.append(next_word)
                        parent_list[next_word].add(word)
                    elif visited[next_word] > visited[word]:
                        parent_list[next_word].add(word)
        
        def dfs(word, path):
            if word == beginWord:
                ans_path.append(path[::-1])
            for next_word in parent_list[word]:
                dfs(next_word, path+[next_word])
        
        dfs(endWord, [endWord])
        return ans_path

        # # 1. Create adjacency list
        # def adjacencyList():

        #     adj = defaultdict(list)
        #     for word in wordList:
        #         for i, _ in enumerate(word):
        #             pattern = word[:i] + "*" + word[i + 1 :]
        #             adj[pattern].append(word)
        #     return adj

        # # 2. Create reversed adjacency list
        # def bfs(adj):

        #     reversedAdj = defaultdict(list)
        #     queue = deque([beginWord])
        #     visited = set([beginWord])

        #     while queue:

        #         visitedCurrentLevel = set()

        #         # Iterate through all words in Queue
        #         for _ in range(len(queue)):

        #             word = queue.popleft()
        #             for i, _ in enumerate(word):

        #                 pattern = word[:i] + "*" + word[i + 1 :]

        #                 for nextWord in adj[pattern]:
        #                     if nextWord not in visited:
        #                         reversedAdj[nextWord].append(word)

        #                         if nextWord not in visitedCurrentLevel:

        #                             # Add such word to the queue
        #                             queue.append(nextWord)
        #                             # Mark such word as visited
        #                             visitedCurrentLevel.add(nextWord)

        #         # Once we done with a level, add all words visited at this level to the visited set
        #         visited.update(visitedCurrentLevel)

        #         if endWord in visited:
        #             break
        #     return reversedAdj

            
        # def dfs(reversedAdj, res, path):

        #     # If the first word in a path is beginWord, we have succesfully constructed a path
        #     if path[0] == beginWord:

        #         # Add such path to the result
        #         res.append(list(path))

        #         return res

        #     word = path[0]

        #     for nextWord in reversedAdj[word]:
        #         path.appendleft(nextWord)
        #         dfs(reversedAdj, res, path)
        #         path.popleft()
        #     return res

        # # Do all three steps
        # adj = adjacencyList()
        # reversedAdj = bfs(adj)
        # res = dfs(reversedAdj, [], deque([endWord]))

        # return res