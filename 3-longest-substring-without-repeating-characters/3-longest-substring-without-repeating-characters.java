import java.util.HashMap;

class Solution {
    public boolean containDuplicate(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (!map.containsKey(s.charAt(i))){
                map.put(s.charAt(i), 1);
            } else {
                return true;
            }
        }
        return false;
    }
    
    public int lengthOfLongestSubstring(String s) {
        if (s.equals("")) return 0;
        
        int ret = 1;
        for (int windowSize = 2; windowSize <= s.length(); windowSize++) {
            boolean stop = true;
            for (int i = 0; i <= s.length() - windowSize; i++) {
                String window = s.substring(i, i + windowSize);
                if (!containDuplicate(window)) {
                    stop = false;
                    break;
                }
            }
            
            if (stop) {
                break;
            } else {
                ret = windowSize;
            }
        }
        return ret;
    }
}