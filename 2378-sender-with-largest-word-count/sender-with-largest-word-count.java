import java.util.*;

class Solution {
    public String largestWordCount(String[] messages, String[] senders) {
        
        int maxCount = 0;
        String ans = "";
        Map<String, List<String>> wordCountMap = new HashMap<>();
        
        int n = messages.length;

        for(int i = 0; i < n; i ++) {
            List<String> msg_list = Arrays.asList(messages[i].split(" "));

            wordCountMap.computeIfAbsent(senders[i], k -> new ArrayList<>())
            .addAll(msg_list);

            
            int currCount = wordCountMap.getOrDefault(senders[i], new ArrayList<>()).size();

            if (maxCount < currCount) {
                maxCount = currCount;
                ans = senders[i];
            }
            else if (maxCount == currCount && senders[i].compareTo(ans) > 0) {
                ans = senders[i];
            }
        }      
        return ans;
    }    
}