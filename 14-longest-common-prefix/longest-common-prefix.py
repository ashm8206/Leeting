class TrieNode:
    def __init__(self):
        self.children = dict()
        self.count = 0
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
   
    def insert(self, wordsList):
        
        for word in wordsList:
            curr = self.root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()

                curr = curr.children[ch] # go to the node,         
                curr.count+=1
                print(ch, curr.count, curr.children)
            
            curr.is_end = True

    def searchLongestPrefix(self):

        curr = self.root
        # if not curr.children:
        #     return ""

        result = []
        while curr and len(curr.children) == 1 and not curr.is_end:
                ch = next(iter(curr.children))
                result.append(ch)
                curr = curr.children[ch]
            # else:
            #     break
        return "".join(result)
            




class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        trie.insert(strs)
        prefix = trie.searchLongestPrefix()
        return prefix

    


# class TrieNode:

#         def __init__(self):
#             self.children = {}
#             self.is_End = False
#             self.links = 0

# class Trie:

#         def __init__(self):
#             self.root = TrieNode()
        
#         def insert(self, word):

#             node = self.root
#             for char in word:
#                 if char not in node.children:
#                     node.children[char] = TrieNode()
#                     node.links+=1
#                 node = node.children[char]
#             node.is_End = True
        
#         def searchLongestPrefix(self, word):
#             node = self.root
#             result = []
#             for char in word:
#                 if char in node.children and node.links == 1 and not node.is_End:
#                     result.append(char)
#                     node = node.children[char]
#                 else:
#                     # no match for next char or Links > 1
#                     break 
#             return "".join(result)

# class Solution:
    
#     def longestCommonPrefix(self, strs: List[str]) -> str:
        

#         # for i in range(strs[0]):
#         #     # for every character in first string, 
#         #     # irrespective of whether we are taking the longest string
#         #     # We will handle that later..

#         #     c = strs[0][i]
#         #     for j in range(1, len(strs)):
#         #         if i == len(strs[j]) or c!=strs[j][i]:
#         #             # return string so far
#         #             return strs[0][0:i]

#         # return strs[0] # entire first string is common 

#         # essentially, we are comparing the until minLen from all 
#         # available strings.
#         # O(n*m) --> but in practice is much smaller than that


#         # TRIE: Approach will be slower in this case
#         # 1st : We build O(n*m) Trie  both space and time
#         # 2nd : We Query on first string, and return the length, uptil the node
#         # that branches into 2+ links.
#         # Branches / Links, is also the # Keys at any level

#         #  Branches in the Trie, stored as # Number of Links, tell us that 
#         # there are two or more variations starting at this point, 
#         # hence the Prefix is no longer Common and we return the length, till
#         # this point

#         trie = Trie()
#         for i in range(1,len(strs)):
#             trie.insert(strs[i])
        
#         if len(strs)==1:
#             return strs[0]
#         return trie.searchLongestPrefix(strs[0])

