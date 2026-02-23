class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxLen = 0
        pathlen = {0:0}

        for line in input.split("\n"):
            name = line.lstrip("\t")
            depth = len(line) - len(name)

            if "." in name: # end of the dirs, we found a file:
                 # a file
                maxLen = max(maxLen, pathlen[depth] + len(name))
            else:
                # either dir
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
            # new subdire = previous_subdir + len(subdr) + 1 --> "/"
        return maxLen