class Solution {
    public String minRemoveToMakeValid(String s) {
        
        
        Stack<Integer> open_index = new Stack<>();
        Set<Integer> index_to_remove = new HashSet<>();
        

        for(int i = 0; i < s.length(); i++) {
            Character ch = s.charAt(i);
            if(Character.isLetter(ch)) {
                continue;
            }
            else if (ch == '(') {
                open_index.add(i);
            }
            else if( ch == ')') {
                if (!open_index.empty()) {
                    open_index.pop();
                }
                else {
                    index_to_remove.add(i);
                }
            }
        }
    
        index_to_remove.addAll(open_index);

        StringBuilder sb =  new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            if(index_to_remove.contains(i)) {
                continue;
            }
            sb.append(s.charAt(i));
        }
        return sb.toString();
    }
}