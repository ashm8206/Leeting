from collections import defaultdict
class Solution:
    def shortestSubstrings(self, arr: list[str]) -> list[str]:

        n = len(arr)
        ans = [""]*n
        all_subtr = defaultdict(set)
        seen = set()

        for i in range(n):
            word_len = len(arr[i])
            word = arr[i]
            for s in range(word_len):
                for e in range(s+1,word_len+1):
                    substr = word[s:e]
                    all_subtr[substr].add(i)
        
        
        for subtr, indices_list in all_subtr.items():
            if len(indices_list)==1:
                # get the word index it belongs to
                idx = next(iter(indices_list))

                if not ans[idx] or len(subtr) < len(ans[idx]) or (len(subtr)== len(ans[idx]) and subtr < ans[idx]):
                    ans[idx] = subtr
        return ans
        #TC:  N * S^2
        #SC: N*S^2


       

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         # Keep track of which strings contain this substring
#         self.string_indices = set()

# class Solution:
#     def shortestSubstrings(self, arr: list[str]) -> list[str]:
#         def insert_all_substrings(s: str, string_idx: int, root: TrieNode):
#             # Insert all possible substrings of s into the trie
#             n = len(s)
#             for i in range(n):  # starting position
#                 for j in range(i + 1, n + 1):  # ending position
#                     curr = root
#                     # Add this substring to trie
#                     for char in s[i:j]:
#                         if char not in curr.children:
#                             curr.children[char] = TrieNode()
#                         curr = curr.children[char]
#                         curr.string_indices.add(string_idx)
        
#         def find_shortest_unique(s: str, string_idx: int, root: TrieNode) -> str:
#             n = len(s)
#             shortest = None
            
#             # Try all possible substrings
#             for i in range(n):  # start
#                 for j in range(i + 1, n + 1):  # end
#                     substr = s[i:j]
                    
#                     # Check if this substring exists in trie and is unique
#                     curr = root
#                     is_unique = True
#                     for char in substr:
#                         if char not in curr.children:
#                             is_unique = False
#                             break
#                         curr = curr.children[char]
                    
#                     if not is_unique:
#                         continue
                        
#                     # Check if this substring only appears in current string
#                     if curr.string_indices == {string_idx}:
#                         if shortest is None or (len(substr) < len(shortest)) or \
#                            (len(substr) == len(shortest) and substr < shortest):
#                             shortest = substr
                            
#             return shortest if shortest else ""

#         # Build trie with all substrings
#         root = TrieNode()
#         for i, s in enumerate(arr):
#             insert_all_substrings(s, i, root)
        
#         # Find shortest unique substring for each string
#         answer = []
#         for i, s in enumerate(arr):
#             answer.append(find_shortest_unique(s, i, root))
            
#         return answer

# class Trie:
#     def __init__(self):
#         self.children = [None] * 26  # Array of 26 possible characters
#         self.first = -1   # Index of first string containing this substring
#         self.second = -1  # Index of second string containing this substring
        
#     def insert(self, s: str, from_idx: int) -> None:
#         # For each possible starting position in string
#         for i in range(len(s)):
#             # For each possible ending position
#             root = self
#             for j in range(i, len(s)):
#                 char_idx = ord(s[j]) - ord('a')
#                 if not root.children[char_idx]:
#                     root.children[char_idx] = Trie()
#                 root = root.children[char_idx]
                
#                 # Track occurrences of this substring
#                 if root.first == -1:
#                     root.first = from_idx
#                 elif from_idx != root.first and root.second == -1:
#                     root.second = from_idx

# class Solution:
#     def shortestSubstrings(self, arr: list[str]) -> list[str]:
#         # Build Trie with all substrings
#         trie = Trie()
#         for i, s in enumerate(arr):
#             trie.insert(s, i)
        
#         # Find shortest unique substring for each string
#         for i in range(len(arr)):
#             min_substr = None
            
#             # Try all possible starting positions
#             for j in range(len(arr[i])):
#                 best = self.sub(arr[i], j, trie, i)
#                 if not best:
#                     continue
                    
#                 # Update if we found a shorter substring or
#                 # lexicographically smaller substring of same length
#                 if (not min_substr or 
#                     len(best) < len(min_substr) or
#                     (len(best) == len(min_substr) and best < min_substr)):
#                     min_substr = best
            
#             arr[i] = min_substr if min_substr else ""
            
#         return arr
    
#     def sub(self, word: str, start: int, trie: Trie, from_id: int) -> str:
#         # Build substring starting at 'start' position until we find
#         # a unique substring (one that appears in only one string)
#         result = []
#         curr_trie = trie
        
#         for i in range(start, len(word)):
#             char_idx = ord(word[i]) - ord('a')
#             curr_trie = curr_trie.children[char_idx]
#             result.append(word[i])
            
#             # If this substring appears in only one string
#             if curr_trie.second == -1:
#                 return ''.join(result)
        
#         return None


# My answer

# class Solution:
#     def shortestSubstrings(self, arr: List[str]) -> List[str]:
        
#         # Trie / Trie Till you succeed.
#         hmap_cand_substr = defaultdict(set)
#         hmap_str_cand = defaultdict(set) 
        

#         for idx, cand in enumerate(arr):
#             hmap_cand_substr[cand].add("")
#             hmap_str_cand[""].add(idx)
#             for i in range(len(cand)):
#                 for j in range(i,len(cand)):
#                     hmap_cand_substr[cand].add(cand[i:j+1])
#                     hmap_str_cand[cand[i:j+1]].add(idx)
        
#         result  = []
        
#         for cand in arr:
#             found = False
#             for value in sorted(hmap_cand_substr[cand], key= lambda x : (len(x), x)):
#                 if len(hmap_str_cand[value]) == 1:
#                     result.append(value)
#                     found = True
#                     break
#             if not found:
#                 result.append("")

#         return result

        # Time: N* N**2LogN**2
        # Space : O(N*N): all substrings




    