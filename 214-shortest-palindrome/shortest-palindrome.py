class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        reversed_string = s[::-1]  # Reverse the string

        # Iterate through the string to find the longest palindromic prefix
        for i in range(length):
            if s[: length - i] == reversed_string[i:]:
                return reversed_string[:i] + s
        return ""
        # length = len(s)
        # if length == 0:
        #     return s

        # # Find the longest palindromic prefix
        # left = 0
        # for right in range(length - 1, -1, -1):
        #     if s[right] == s[left]:
        #         left += 1

        # # If the whole string is a palindrome, return the original string
        # if left == length:
        #     return s

        # # Extract the suffix that is not part of the palindromic prefix
        # non_palindrome_suffix = s[left:]
        # reverse_suffix = non_palindrome_suffix[::-1]

        # # Form the shortest palindrome by prepending the reversed suffix
        # return (
        #     reverse_suffix
        #     + self.shortestPalindrome(s[:left])
        #     + non_palindrome_suffix
        # )