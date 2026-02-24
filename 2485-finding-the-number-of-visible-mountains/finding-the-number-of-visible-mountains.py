class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        # count frequency for each point
        count = Counter((x, y) for x, y in peaks)

        if not peaks:
            return 0

        peaks = sorted([k for k, _ in count.items()])

        def within(peak1, peak2):
            # return True if `pa` is within `pb`
            x1, y1 = peak1
            x2, y2 = peak2
            return y1 - x1 <= y2 - x2 and x1 + y1 <= x2 + y2

        stack = []
        for i, peak in enumerate(peaks):
            # because you are no t storing bases, you have to try both
            while stack and within(stack[-1], peak):

                stack.pop()

            if stack and within(peak, stack[-1]):
                # dont keep the peak that is hidden
                continue
            stack.append(peak)

        stack = [v for v in stack if count[v]==1]
        return len(stack)