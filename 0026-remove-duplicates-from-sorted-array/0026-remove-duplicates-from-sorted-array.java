class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        int temp = 101;
        
        for(int e:nums) {
            if (e == temp) {
                continue;
            }
            
            temp = e;
            nums[i] = temp;
            i++;
        }
        return i;
    }
}