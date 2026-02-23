class Solution {
    public String removeStars(String s) {

        StringBuilder sb = new StringBuilder();

        for (char c: s.toCharArray()){
            if(!sb.isEmpty() && c == '*') {
                sb.deleteCharAt(sb.length()-1);
            }
            else {
                sb.append(c);
            }

        }

        return sb.toString();
    }
}