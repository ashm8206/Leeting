class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()
        self.n = 0
    # def __str__(self):
    #     return str(self.children) + str(self.words)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add_word(self, word):
        node = self.root

        """At root Level
        We have empty key, the first char in the Trie, is a child of Empty key
        { : children { m: children: {o}} , words=[]} At root Level"""
        
        for c in word:
            if c not in node.children: 
                node.children[c] = TrieNode()

            node = node.children[c] 
           
            
            if node.n < 3:
                node.words.append(word)
                node.n += 1
        
    def find_word_by_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c] 
            else: #--> return empty list
                return []
            
            """
            Another way of writing the above is:
            
            if c not in node.children:
                return []
            node = node.children[char] --> every time!!

            This saves the if / else as 
            its saves time for us from checking common condition again and again
            through multiple 'ifss'
            """
        return node.words  # only return at after entire prefix is matched
            
class Solution:
    def suggestedProducts(self, A: List[str], searchWord: str) -> List[List[str]]:
        # Method  I
        # A.sort()
        """
        Sorting is important, to return lexographically ordered suggestion

        It is important to process words in order, as we add words at each level
        upto size 3

        To make sure, the correct lexographically words are adde as the Top 3 suggestions, (similar to oxford dict, it helps to have the input sorted)
        """
        # trie = Trie()
        # for word in A: trie.add_word(word)
    
        # result, prefix = [], ''
        # for c in searchWord:
        #     prefix += c 
        #     result.append(trie.find_word_by_prefix(prefix))
        # return result    

        """A Note on Time Complexity

        # Time : 
            1. Sort : Nlogn

            2. Building trie:   N words of Len M == O(N*M)
            If there are many words that are prefixes of each other --Tend to --> O(M), where M is Len of Prefix

        # Space : Space will also be same as build, with the same constraints/qualifiers incase of common prefixes (m), vs No common prefixes (n*m)
        """

        # Method II - LeftMost Binary Search

        A.sort()
        res, prefix = [], ''
        i = 0
        for c in searchWord: 
            prefix += c
            i = bisect.bisect_left(A, prefix, lo=i) # M*LogN
            # we get left most index of prefix in the search
            # and ad next 3 product that match prefix
            
            #  An optimization: 
            #  passing lo : start index
            #  In each Binary serach, it is not required to start lo = 0
            #  Lo = atleast as small as the "i" from previous prefix matched

            res.append([w for w in A[i:i+3] if w.startswith(prefix)]) #--> o(3)*O(k)
        return res

        # TC : 
        # 1. Sort : NlogN 
        # 2  PrefixSearch : O(M len of Prefix)*Log(N) Binsearch
        # 3 startswith