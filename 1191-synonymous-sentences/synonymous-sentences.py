class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
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
        
        components = defaultdict(list)

        for idx in range(0, n):
            visited = set()
            dfs(visited, array[idx])
            components[idx].extend(visited)
        
        # print(components)
            

        def backtrack(slate, idx):

            if idx==n:
                res.append(" ".join(slate[:]))
                return
            
            wordlist = components[idx]
            
            for word in wordlist:
                slate.append(word)
                backtrack(slate, idx+1)
                slate.pop()
            
        

        backtrack([], 0)

        return sorted(res)