class Solution {
    public int removeDuplicates(int[] nums) {
        int insert = 0;
        int temp = 101;
        
        for(int i = 0; i < nums.length; i++) {
            if (nums[i] == temp) {
                continue;
            }
            
            temp = nums[i];
            nums[insert] = temp;
            insert++;
        }
        return insert;
    }
}