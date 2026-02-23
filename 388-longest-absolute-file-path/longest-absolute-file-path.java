class Solution {
    public int lengthLongestPath(String input) {

        int maxLen =  0;
        String [] lines = input.split("\n");
        Map<Integer,Integer> pathlen = new HashMap<>();
        pathlen.put(0,0);

        for(String line: lines) {
            // String name = line.strip("\t"); --> doesnt work
            // removes tabs
            String name = line.replaceAll("\t", "");

            // Removes tab from start or end
            // String name = line.replaceAll("^\t+|\t+$", "");
            Integer depth = line.length() - name.length();

            if (name.contains(".")){
                maxLen = Math.max(maxLen, pathlen.get(depth) + name.length());
            }
            else {
                Integer val = pathlen.get(depth) + name.length() + 1;
                pathlen.put(depth+1, val);
            }
        
        }

        return maxLen;
    }
}