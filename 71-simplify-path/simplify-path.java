class Solution {
    public String simplifyPath(String path) {
        String[] a = path.split("/");
        List<String> res = new ArrayList<>();

        for(String val : a) {
            if(val.equals(".") || val.isEmpty()) {
                continue;
            }
            else if(val.equals("..")) {
                if(!res.isEmpty()) {
                    res.removeLast();
                }
               
            }
            else {
                res.add(val);
            }

        }
        return "/" + String.join("/", res);
    }
}