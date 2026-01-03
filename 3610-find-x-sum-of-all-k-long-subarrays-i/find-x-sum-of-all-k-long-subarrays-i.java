class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        int n = nums.length;
        int windowSize = n-k+1;
        int[] res = new int[windowSize];
        
        
        for(int i = 0 ; i <  windowSize; i++) {
            res[i] = topKSum(nums, i, i+k, x);
        }
        return res;
    }

    public int topKSum(int[] nums, int start, int end, int x) {

        // Step 1: Count frequencies
        Map<Integer, Integer> freq = new HashMap<>();
        for(int i = start; i < end; i++) {
            freq.merge(nums[i], 1, Integer::sum);
        }

        // Step 2: Use min-heap to keep top K
        PriorityQueue<Map.Entry<Integer, Integer>> minHeap = 
            new PriorityQueue<>((a, b) -> {
                if (a.getValue()!=b.getValue()) return a.getValue() - b.getValue();
                return a.getKey() - b.getKey();
        }); // min-heap by frequency with tie breaker

        for (Map.Entry entry : freq.entrySet()) {
            minHeap.offer(entry);
            if (minHeap.size() > x) {
                minHeap.poll(); // remove least frequent
            }
        }
        int ans = 0;
        for(Map.Entry<Integer, Integer> entry : minHeap) {
            int curr = entry.getKey() * entry.getValue();  
            ans = ans + curr;
            // System.out.println(entry.getKey() + "  " + entry.getValue());
        }
        // System.out.println("****");
    return ans;
    }

// Now minHeap contains top K most frequent elements
}