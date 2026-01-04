class Solution {
    public int[] findOriginalArray(int[] changed) {
        if(changed.length%2 == 1) {
            return new int[0];
        }

        Arrays.sort(changed);
        Map<Integer, Integer> freq = new HashMap<>();
        for(int num: changed){
            freq.put(num, freq.getOrDefault(num, 0)+1);
        }
        int[] ans = new int[changed.length/2];
        int index = 0;

        for (int num : changed) {
            // If element exists
            if (freq.get(num) > 0) {
				freq.put(num, freq.get(num) - 1);
                int twiceNum = num * 2;
                if (freq.containsKey(twiceNum) && freq.get(twiceNum) > 0) {
                    // Pair up the elements, decrement the count
                    freq.put(twiceNum, freq.get(twiceNum) - 1);
                    // Add the original number to answer
                    ans[index++] = num;
                } else {
                    return new int[0];
                }
            }
        }
        
        return ans;
    }
}