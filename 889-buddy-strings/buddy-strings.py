class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        A = s
        B = goal
        # Case 1: If lengths are different, impossible to make equal with swaps
        if len(A) != len(B):
            return False
            
        # Case 2: If strings are identical
        if A == B:
            # Need at least one repeated character to make a valid swap
            # len(set(A)) < len(A) checks if there are any duplicates
            # Example: "aab" -> set("aab") = {"a","b"} -> len=2 < len("aab")=3
            return len(set(A)) < len(A)
        
        # Case 3: For different strings, find all positions with different characters
        # zip(A, B) pairs up corresponding characters from both strings
        # Create list of tuples (a, b) where characters differ
        # Example: A="ab", B="ba" → dif=[('a','b'), ('b','a')]
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        
        # For a valid buddy string:
        # 1. Must have exactly 2 differences
        # 2. First difference reversed must equal second difference
        # Example: dif=[('a','b'), ('b','a')]
        #         dif[0] = ('a','b')
        #         dif[1][::-1] = ('b','a')[::-1] = ('a','b')
        return len(dif) == 2 and dif[1] == dif[0][::-1]




        # if len(s)!= len(goal) or set(s) != set(goal): return False 

        # if s == goal:
        #     # If we have 2 same characters in string 's',
        #     # we can swap them and still the strings will remain equal.
        #     frequency = [0] * 26
        #     for ch in s:
        #         frequency[ord(ch) - ord('a')] += 1
        #         if frequency[ord(ch) - ord('a')] == 2:
        #             return True
        #     # Otherwise, if we swap any two characters, it will make the strings unequal.
        #     return False
        # else:

        #     indices = []
        #     counter = 0
        #     for i in range(len(s)):
        #         if s[i] != goal[i]:
        #             counter += 1
        #             indices.append(i)       
        #         if counter > 2:
        #             return False       
        #     return s[indices[0]] == goal[indices[1]] and s[indices[1]] == goal[indices[0]]

        




        