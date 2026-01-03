from collections import defaultdict
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        # case- sensitive
        # wordcount ==  sort(count, key)
        # alice = 3 and Alice = 3

        maxCount = 0
        ans = ""
        wordCountMap = defaultdict(list)

        for msg, sender in zip(messages, senders):
            msg_list = msg.split(" ")
            wordCountMap[sender].extend(msg_list)
            
            currCount = len(wordCountMap[sender])
            if maxCount < currCount:
                maxCount = currCount
                ans = sender
            elif maxCount == currCount:
                ans = max(ans, sender)
        return ans


