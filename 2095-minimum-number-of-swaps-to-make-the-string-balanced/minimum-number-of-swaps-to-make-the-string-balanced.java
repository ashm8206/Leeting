class Solution {
    public int minSwaps(String s) {

        // 0  1  2  3  4  5
        // ]  ]  ]  [  [  [
        // [. ]. ] [.  [ ]
        //

        // op : len(op)
        // swap: len(cl), cl > op

        // since string consists of n/2 and n/2 you can return either

        Stack<Integer> st = new Stack<>();
        Set<Integer> close_to_remove = new HashSet<>();

        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if (ch == '[') {
                st.add(i);
            }
            else {
                if(!st.empty()){
                    st.pop();
                }
                else {
                    close_to_remove.add(i);
                }
            }
            
        }
        // # each swap fixes two, +1 for odd number sneeds 1 more
        return (close_to_remove.size() + 1)/ 2;
        
    }
}