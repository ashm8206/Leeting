class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (
            endWord not in wordList
            or not endWord
            or not beginWord
            or not wordList
        ):
            return 0

        L = len(beginWord)
        
        all_comb = defaultdict(list)

        for word in wordList:
            for i in range(L):

                all_comb[word[:i]+"*"+word[i+1:]].append(word)
        # print(all_comb)
        visited = set()
        q = deque()
        q.append((beginWord, 1))

        while q:
            curr_word, level = q.popleft()

            visited.add(curr_word)

            if curr_word == endWord:
                return level


            for i in range(L):
                key = curr_word[:i]+"*"+curr_word[i+1:]
                if key in all_comb:
                    for next_word in all_comb[key]:
                        if next_word not in visited:
                            q.append((next_word, level+1))
                    # all_comb[key] = []
    
        return 0



    

        