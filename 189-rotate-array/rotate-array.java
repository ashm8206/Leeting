class Solution {

    public void reverseArray(int[] nums, int left, int right) {
        int temp = 0;
        while (left < right) {
            temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left  += 1;
            right -= 1;

        }

    }
    public void rotate(int[] nums, int k) {

        int n = nums.length;
        k = k % n;

        reverseArray(nums, 0, n - k -1);
        reverseArray(nums, n - k, n-1);
        reverseArray(nums, 0, n-1);

        // [1,2,3,4,5,6,7] 
        // [4,3,2,1] [0... n - k - 1]
        // [7, 6, 5] [n - k, n-1]
        // [4, 3, 2, 1, 7, 6, 5]
        // [5, 6, 7, 1, 2, 3, 4] [0... n - 1]

    
    }   
}