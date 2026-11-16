class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> complements = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (complements.containsKey(complement)) {
                int[] ans = {complements.get(complement), i};
                return ans;
            }
            complements.put(nums[i], i);
        }
        return new int[]{};
    }
}
