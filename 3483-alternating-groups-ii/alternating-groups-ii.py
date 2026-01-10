class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        extended = colors[:] + colors[:k-1]
        # k = 3
        # first element: colors[n-1]
        #  2nd element: colors[0]
        #  3rd element: colors[1]  # need only k-1 elemets
        result = 0

        alternating_elem = 1

        last_color = colors[0]

        for index in range(1, len(extended)):

            # Check if current color is the same as the last color
            if extended[index] == last_color:
                # Pattern breaks, reset sequence length
                alternating_elem = 1
                last_color = extended[index]
                continue

            # Extend sequence
            alternating_elem += 1

            # If sequence length reaches at least k, count it
            if alternating_elem >= k:
                result += 1
            
            last_color = extended[index]
        return result