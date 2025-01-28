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
        self.curr_node = self.root # curr_node
        self.dead = TrieNode() 
        # stop search if one prefix not found

    def add_sentence(self, sentence, count):

        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.sentences[sentence] += count 
    
    def input(self, c: str) -> List[str]:

        if c == "#":
    
            curr_sentence = "".join(self.curr_sentence)
            self.add_sentence(curr_sentence, 1)
            self.curr_sentence = [] # typed sentence storing
            self.curr_node = self.root
            self.dead = TrieNode() 
            return []
        else:
            self.curr_sentence.append(c)
            if c in self.curr_node.children:
                self.curr_node = self.curr_node.children[c]
                res = sorted(self.curr_node.sentences.items(), key=(lambda x: (-x[1],x[0])))[:3]
                res = [ k for k, v in res]
                return res
            else:
                self.curr_node = self.dead
                return []
        
        
       
        
        # self.curr_node = self.curr_node.children[c]
        # items = [(-val, key) for key, val in self.curr_node.sentences.items()]
        # ans = heapq.nsmallest(3, items)
        # return [key for count, key in ans]



# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)