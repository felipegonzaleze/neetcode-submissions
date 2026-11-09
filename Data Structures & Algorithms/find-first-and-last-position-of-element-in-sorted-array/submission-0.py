class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        for num in nums:
            if nums[left] != target:
                left += 1
            if nums[right] != target:
                right -= 1
        return [left, right]