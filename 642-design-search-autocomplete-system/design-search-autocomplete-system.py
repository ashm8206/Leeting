class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        for sentence, count in zip(sentences, times):
            self.add_sentence(sentence,count)
        
        self.curr_sentence = [] # typed sentence storing
        self.curr_node = self.root 
        self.dead = TrieNode() 

    def add_sentence(self, sentence, count):

        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            # node.sentences.append((-count, sentence))
            node.sentences[sentence] += count 
            # node.sentences[sentence] += count # this is -ve for the heap
    
    def input(self, c: str) -> List[str]:

        if c == "#":
            # Returns an empty array []  
            # stores the inputted sentence in the system.

            curr_sentence = "".join(self.curr_sentence)
            self.add_sentence(curr_sentence, 1)
            self.curr_sentence = [] # typed sentence storing
            self.curr_node = self.root
            self.dead = TrieNode() 
            return []
        
        self.curr_sentence.append(c)
        if c not in self.curr_node.children:
            self.curr_node = self.dead
            # don't find anything else, assign dead node, return
            return []
        
        self.curr_node = self.curr_node.children[c]
        items = [(-val, key) for key, val in self.curr_node.sentences.items()]
        ans = heapq.nsmallest(3, items)
        return [key for count, key in ans]



# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)