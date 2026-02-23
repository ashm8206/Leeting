class Solution {
    public String decodeString(String s) {
        Stack<String> st = new Stack();

        for (char ch : s.toCharArray()){
            if (ch == ']') {
                String curr_str = "";
                String curr_int = "";

                while (!st.isEmpty() && !st.peek().equals("[")) {
                    curr_str = st.pop() + curr_str;
                }
                st.pop(); // "["

                while (!st.isEmpty() && Character.isDigit(st.peek().charAt(0))) {
                    curr_int = st.pop() + curr_int;
                }

                int count = Integer.parseInt(curr_int);
                st.add(curr_str.repeat(count));



            }
            else {
                // digit
                // [
                //char
                st.add(String.valueOf(ch));
            }
        }
    return String.join("", st);
    }
}