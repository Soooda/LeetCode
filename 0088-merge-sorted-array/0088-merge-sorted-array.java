class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] temp = new int[m];
        for (int i = 0; i < m; i++) {
            temp[i] = nums1[i];
        }
        
        int idx1 = 0;
        int idx2 = 0;
        
        for (int i = 0; i < m + n; i++) {
            if (idx1 == m && idx2 == n) {
                break;
            } else if (idx1 == m) {
                nums1[i] = nums2[idx2];
                idx2++;
            } else if (idx2 == n) {
                nums1[i] = temp[idx1];
                idx1++;
            } else if (temp[idx1] < nums2[idx2]) {
                nums1[i] = temp[idx1];
                idx1++;
            } else {
                nums1[i] = nums2[idx2];
                idx2++;
            }
        }
    }
}