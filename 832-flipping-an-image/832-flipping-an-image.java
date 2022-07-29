class Solution {
    public static int[] flip(int[] a) {
        int[] result = new int[a.length];
        
        int index = 0;
        for(int i = a.length - 1; i >= 0; i--) {
            result[index] = a[i];
            index++;
        }
        
        return result;
    }
    
    public static int[][] invert(int[][] a) {
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                if(a[i][j] == 0) {
                    a[i][j] = 1;
                } else {
                    a[i][j] = 0;
                }
            }
        }
        
        return a;
    }
    
    public int[][] flipAndInvertImage(int[][] A) {
        for(int i = 0; i < A.length; i++){
            A[i] = flip(A[i]);
        }
        
        A = invert(A);
        
        return A;
    }
    
}