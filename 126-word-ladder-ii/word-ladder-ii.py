from collections import defaultdict, deque


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> list[list[str]]:
        # Check if endWord exists in wordList
        if endWord not in wordList:
            return []
            
        # Add beginWord to wordList if not present
        wordSet = set(wordList)
        if beginWord not in wordSet:
            wordSet.add(beginWord)
            
        wordDict = defaultdict(set)
        # Build pattern dictionary
        for word in wordSet:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                wordDict[pattern].add(word)

        # BFS setup
        queue = deque([beginWord])
        visited = {beginWord: 1}  # word: level
        reverse_adj = defaultdict(set)  # child: {parents}
        found = False

        # BFS traversal
        while queue and not found:
            level_size = len(queue)
            # Process all nodes at current level
            for _ in range(level_size):
                curr_word = queue.popleft()
                curr_level = visited[curr_word]
                
                # Generate all possible patterns
                for i in range(len(curr_word)):
                    pattern = curr_word[:i] + "*" + curr_word[i+1:]
                    
                    # Check all words matching this pattern
                    for next_word in wordDict[pattern]:
                        # Skip self-loops
                        if next_word == curr_word:
                            continue
                            
                        # Target found
                        if next_word == endWord:
                            found = True
                            visited[next_word] = curr_level + 1
                            reverse_adj[next_word].add(curr_word)
                            
                            
                        # New word discovered
                        elif next_word not in visited:
                            queue.append(next_word)
                            visited[next_word] = curr_level + 1
                            reverse_adj[next_word].add(curr_word)
                            
                        # Alternative path of same length
                        elif visited[next_word] == curr_level + 1:
                            reverse_adj[next_word].add(curr_word)

        # No path found
        if endWord not in reverse_adj:
            return []

        # Build paths using DFS
        ans_paths = []
        
        def dfs(word, path):
            if word == beginWord:
                ans_paths.append(path[::-1])
                return
                
            for parent in reverse_adj[word]:
                dfs(parent, path + [parent])
        
        # Start DFS from endWord
        dfs(endWord, [endWord])
        return ans_paths

