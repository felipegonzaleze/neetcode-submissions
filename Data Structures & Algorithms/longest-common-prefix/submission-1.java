class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = "";
        int length = strs[0].length();

        for (int i = 0; i < length; i++) {
            Character current = strs[0].charAt(i);
            for (int j = 0; j < strs.length; j++) {
                if (i == strs[j].length() || strs[j].charAt(i) != current) {
                    return prefix;
                }
            }
            prefix += current;
        }
        return prefix;
    }
}