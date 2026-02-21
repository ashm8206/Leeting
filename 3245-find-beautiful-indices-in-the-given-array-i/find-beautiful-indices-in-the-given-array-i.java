class Solution {
    public List<Integer> beautifulIndices(String s, String a, String b, int k) {
        
        int n = s.length();
        int na = a.length();
        int nb = b.length();
        List<Integer> res = new ArrayList<>();

        List<Integer> aIdx = new ArrayList<>();
        List<Integer> bIdx = new ArrayList<>();


        for(Integer i=0; i < n-na+1; i++) {
            String currA = s.substring(i, i+na);
            if (currA.equals(a)) {
                aIdx.add(i);
            }
        }

        for(Integer j=0; j < n-nb+1; j++) {
            String currB = s.substring(j, j+nb);
            if (currB.equals(b)) {
                bIdx.add(j);
            }
        }

        for(Integer i: aIdx){
            for(Integer j: bIdx) {
                if(Math.abs(j-i) <= k) {
                    res.add(i);
                    break;
                }
            }
        }
        
       return res; 
    }
}