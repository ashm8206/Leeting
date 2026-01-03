class Solution {
    public int arithmeticTriplets(int[] nums, int diff) {
        
        Set<Integer> set = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        
        int count = 0;
        for(int numI: nums){
            int numJ = numI + diff;
            int numK = numJ + diff;
            if(set.contains(numJ) && set.contains(numK)) {
                count+=1;
            }
            
        }
        return count;
    }
}