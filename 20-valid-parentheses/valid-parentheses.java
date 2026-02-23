class Solution {
    public boolean isValid(String s) {
        
        Map<Character, Character> hmap = new HashMap<>();
        hmap.put(')','(');
        hmap.put(']','[');
        hmap.put('}','{');

        Stack<Character> st = new Stack<>();
        for(char ch : s.toCharArray()) {
            if (hmap.containsKey(ch)) {
                if (!st.isEmpty() &&  st.peek() == hmap.get(ch)) {
                    st.pop();
                    continue;
                }
                return false;

            }
            else {
                //opening brack add
                st.add(ch);
            }
        }
        return st.empty() ? true : false;
    }
}