class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        found = False
        left = 0
        right = len(nums) - 1
        for num in nums:
            if nums[left] != target:
                left += 1
            if nums[right] != target:
                right -= 1
            if num == target:
                found = True
        if found:
            return [left, right]
        else:
            return [-1, -1]