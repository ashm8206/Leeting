import java.util.*;

class Solution {
    public String largestWordCount(String[] messages, String[] senders) {
        
        int maxCount = 0;
        String ans = "";
        // Map<String, List<String>> wordCountMap = new HashMap<>();
        Map<String, Integer> wordCountMap = new HashMap<>();
        
        int n = messages.length;

        for(int i = 0; i < n; i ++) {
            // List<String> msg_list = Arrays.asList(messages[i].split(" "));
            // wordCountMap.computeIfAbsent(senders[i], k -> new ArrayList<>())
            // .addAll(msg_list);
            // int totalWords = wordCountMap.getOrDefault(senders[i], new ArrayList<>()).size();

            int currWords = messages[i].split(" ").length;
            int totalWords = wordCountMap.merge(senders[i], currWords, Integer::sum);

            if (maxCount < totalWords || (maxCount == totalWords && senders[i].compareTo(ans) > 0)) {
                maxCount = totalWords;
                ans = senders[i];
            }
        }      
        return ans;
    }    
}