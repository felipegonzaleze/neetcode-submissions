class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid
            elif right - left <= 1:
                break
        print(left, mid, right)
        if nums[mid] == target:
            return mid
        else:
            if left > right:
                return left
            else:
                return right - left
