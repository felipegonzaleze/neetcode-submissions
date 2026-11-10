class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        starter = 0
        ending = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                starter = mid
                ending = mid
                while starter > 0 and nums[starter - 1] == target:
                    starter -= 1
                while ending + 1 < len(nums) and nums[ending + 1] == target:
                    ending += 1
                return [starter, ending]
        return [-1, -1]