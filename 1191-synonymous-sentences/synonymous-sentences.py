from collections import defaultdict, deque
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # # Build a graph of synonyms (adjacency list)
        # graph = defaultdict(list)
        # for pair in synonyms:
        #     w1, w2 = pair
        #     self.connect(graph, w1, w2)
        #     self.connect(graph, w2, w1)

        # # BFS to generate all possible sentences
        # ans = set()
        # q = deque([text])
        # while q:
        #     current_sentence = q.popleft()
        #     ans.add(current_sentence)  # Add to result set
        #     words = current_sentence.split()

        #     # Try replacing each word with its synonym
        #     for i in range(len(words)):
        #         if words[i] not in graph:
        #             continue
        #         for synonym in graph[words[i]]:
        #             words[i] = synonym
        #             new_sentence = ' '.join(words)
        #             if new_sentence not in ans:
        #                 q.append(new_sentence)
        #         words[i] = current_sentence.split()[i]  # Restore the original word

        # return sorted(ans)  # Return the result as a sorted list

    # def connect(self, graph, v1, v2):
    #     graph[v1].append(v2)

        #Output will be all possible sentences with synonyms replaced

        
        if not synonyms or not text:
            return text
        
        graph = defaultdict(list)

        #build graph
        for w1, w2 in synonyms:
            graph[w1].append(w2)
            graph[w2].append(w1)

        
        res = []
        array = text.split(" ")
        n = len(array)

        def dfs(visited, word):

            visited.add(word)

            for nei in graph[word]:
                if nei not in visited:
                    dfs(visited, nei)
        

        # Get Components, 
        # We are Only interested in Getting Components with "Root" present in the Text
        components = defaultdict(list)

        for idx in range(0, n): # O(n*m)
            visited = set()
            dfs(visited, array[idx])
            components[idx].extend(visited)
        

        def backtrack(slate, idx): # M^N

            if idx==n:
                res.append(" ".join(slate[:]))
                return
            
            wordlist = components[idx]
            
            for word in wordlist:
                slate.append(word)
                backtrack(slate, idx+1)
                slate.pop()
            
        

        backtrack([], 0)

        return sorted(res) # NLOGN