class Solution {
    public boolean checkValidString(String s) {

        Stack<Integer> open_index = new Stack<>();
        Stack<Integer> star_idx = new Stack<>();
        

        for(int i = 0; i < s.length(); i++) {
            Character ch = s.charAt(i);
            if(ch == '*') {
                star_idx.add(i);
            }
            else if (ch == '(') {
                open_index.add(i);
            }
            else  {
                if (!open_index.isEmpty()) {
                    open_index.pop();
                }
                else if (!star_idx.isEmpty()){
                    star_idx.pop();
                }
                else {
                    return false;
                }
            }     
        }

        // System.out.print(open_index);
        // System.out.println(star_idx);
        
        while(!open_index.isEmpty() && !star_idx.isEmpty()) {
            if(open_index.pop() > star_idx.pop()) {
                // System.out.print(open_index);
                // System.out.println(star_idx);
                return false;  // Star comes before '(', can't use as ')'
            } 
        }
    
    return open_index.isEmpty();
    }
} 