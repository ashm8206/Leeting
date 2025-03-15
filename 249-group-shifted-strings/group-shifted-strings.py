class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        mp = defaultdict(list)
        for s in strings:
            key = tuple((ord(c)-ord(s[0])+26)%26 for c in s)
            mp[key].append(s)
    
        return list(mp.values())

        # Same key: circular shifts
        # "abc" -> key = (0, 1, 2)
        # "xyz" -> key = (0, 1, 2)  # Because of circular wrap

        # Cyclic Behavior:
        # # Always returns a value in range [0, b-1]
        # print(7 % 3)    # 1
        # print(10 % 3)   # 1
        # print(13 % 3)   # 1

        # Negative Number Handling:
        # Always same sign as divisor
        # print(-1 % 26)  # 25 (not -1)
        # print(-2 % 26)  # 24
