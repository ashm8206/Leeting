class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # WHY IS THIS NOT RECURSIVE?
        # - One clear optimal strategy: remove higher-value pattern first
        # - No overlapping subproblems: once you choose order, just execute
        # - No dependencies: removing "ab" doesnt affect ability to remove "ba"

        total_score = 0
        high_priority_pair = "ab" if x > y else "ba"
        low_priority_pair = "ba" if high_priority_pair == "ab" else "ab"

        # First pass: remove high priority pair
        string_after_first_pass = self.remove_substring(s, high_priority_pair)
        removed_pairs_count = (len(s) - len(string_after_first_pass)) // 2

        # Calculate score from first pass
        total_score += removed_pairs_count * max(x, y)

        # Second pass: remove low priority pair
        string_after_second_pass = self.remove_substring(
            string_after_first_pass, low_priority_pair
        )
        removed_pairs_count = (
            len(string_after_first_pass) - len(string_after_second_pass)
        ) // 2

        # Calculate score from second pass
        total_score += removed_pairs_count * min(x, y)

        return total_score

    def remove_substring(self, input: str, target_pair: str) -> str:
        stack = []

        for ch in input:
            if (
                ch == target_pair[1]
                and stack
                and stack[-1] == target_pair[0]
            ):
                stack.pop()  # Remove the matching character from the stack
            else:
                stack.append(ch)

        # Reconstruct the remaining string after removing target pairs
        return "".join(stack)

