class Solution {
    public int similarPairs(String[] words) {

        Map<Set<Character>, Integer> map = new HashMap<>();
        int countPairs = 0;
        for(String word: words) {
            Set<Character> key = getSignature(word);
            if (map.containsKey(key)){
                countPairs += map.get(key);
                map.merge(key, 1, Integer::sum);
            }
            else {
                map.put(key, 1);
            }

        }
        return countPairs;
    }

    public Set<Character> getSignature(String word) {
        Set<Character> set = new HashSet<>();
        for(int i = 0; i < word.length(); i++) {
            set.add(word.charAt(i));
            // for Set<String>
            // Convert char to String 
           // set.add(String.valueOf(word.charAt(i))); 
        }
        return Set.copyOf(set);
    }

}